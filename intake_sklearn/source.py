from intake.source.base import DataSource, Schema
import joblib
import fsspec
import sklearn
import re
import warnings

from . import __version__

class SklearnModelSource(DataSource):
    container = 'python'
    name = 'sklearn'
    version = __version__
    partition_access = False

    def __init__(self, urlpath, storage_options=None, metadata=None):
        """
        Parameters
        ----------

        urlpath: str, location of model pkl file
        Either the absolute or relative path to the file or URL to be
        opened. Some examples:
          - ``{{ CATALOG_DIR }}models/model.pkl``
          - ``s3://some-bucket/models/model.pkl``
        """

        self._urlpath = urlpath
        self._storage_options = storage_options or {}

        super().__init__(metadata=metadata)

    def _load(self):
        with fsspec.open(self._urlpath, mode='rb', **self._storage_options) as f:
            return f.read()

    def _get_schema(self):
        as_binary = self._load()
        if b'_sklearn_version' in as_binary:
            s = re.search(b'_sklearn_versionq(.*\x00)((\d+\.)?(\d+\.)?(\*|\d+))q', as_binary)
            sklearn_version = s.group(2).decode()
        else:
            sklearn_version = None

        self._schema = Schema(
            npartitions=1,
            extra_metadata={
                'sklearn_version':sklearn_version
            }
        )
        return self._schema


    def read(self):
        self._load_metadata()

        if not self.metadata['sklearn_version'] == sklearn.__version__:
            msg = ('The model was created with Scikit-Learn version {}'
                   'but version {} has been installed in your current environment.'
                   'The model may not load or work correctly.').format(self.metadata['sklearn_version'],
                                          sklearn.__version__)
            warnings.warn(msg, RuntimeWarning, stacklevel=2)


        with fsspec.open(self._urlpath, **self._storage_options) as f:
            return joblib.load(f)

