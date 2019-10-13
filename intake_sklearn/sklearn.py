from intake.source.base import DataSource
import joblib
import fsspec

from . import __version__

class SklearnModelSource(DataSource):
    container = 'python'
    name = 'sklearn'
    version = __version__
    partition_access = False

    def __init__(self, urlpath, metadata=None):
        """
        Parameters
        ----------

        urlpath: str, location of model pkl file
        Either the absolute or relative path to the file or URL to be
        opened. Some examples:
          - ``{{ CATALOG_DIR }}models/model.pkl``
          - ``s3://some-bucket/models/model.pkl``
        """

        self.urlpath = urlpath

        super().__init__(metadata=metadata)


    def read(self):
        self._load_metadata()

        with fsspec.open(self.urlpath): as f:
            return joblib.load(f)

