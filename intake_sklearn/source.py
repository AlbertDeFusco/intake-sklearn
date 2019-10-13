from intake.source.base import DataSource
import joblib
import fsspec

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


    def read(self):
        self._load_metadata()

        with fsspec.open(self._urlpath, storage_options=self._storage_options): as f:
            return joblib.load(f)

