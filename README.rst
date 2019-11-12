===============================
intake_sklearn
===============================


.. image:: https://img.shields.io/travis/albertdefusco/intake_sklearn.svg
        :target: https://travis-ci.org/albertdefusco/intake_sklearn
.. image:: https://codecov.io/gh/albertdefusco/intake_sklearn/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/albertdefusco/intake_sklearn


Intake plugin to load Scikit-Learn model pickle files

# Model catalogs

* Declare locations of model pickle files
* Declare required packages and check for version compatibility
* Standardize model loading for various model types
    * Scikit-Learn, and eventually XGBoost, Keras/Tensorflow, Dask-ML, etc.

## Sklearn driver


```python
import intake

model_source = intake.open_sklearn('optimized_model.pkl')
model_source
```

```
<intake_sklearn.source.SklearnModelSource at 0x1143d7a50>
```



```python
model = model_source.read()
model
```


```
    Pipeline(memory=None,
             steps=[('standardscaler',
                     StandardScaler(copy=True, with_mean=True, with_std=True)),
                    ('gradientboostingregressor',
                     GradientBoostingRegressor(alpha=0.9, criterion='friedman_mse',
                                               init=None, learning_rate=0.1,
                                               loss='ls', max_depth=3,
                                               max_features=None,
                                               max_leaf_nodes=None,
                                               min_impurity_decrease=0.0,
                                               min_impurity_split=None,
                                               min_samples_leaf=1,
                                               min_samples_split=2,
                                               min_weight_fraction_leaf=0.0,
                                               n_estimators=100,
                                               n_iter_no_change=None,
                                               presort='auto', random_state=None,
                                               subsample=1.0, tol=0.0001,
                                               validation_fraction=0.1, verbose=0,
                                               warm_start=False))],
             verbose=False)
```


## Incompatible versions?


```python
old_model_source = intake.open_sklearn('old_model.pkl')
old_model_source.read()
```

```
    ---------------------------------------------------------------------------

    RuntimeError                              Traceback (most recent call last)

    <ipython-input-3-5b1fd5628c1f> in <module>
          1 old_model_source = intake.open_sklearn('old_model.pkl')
    ----> 2 old_model_source.read()
    

    ~/Development/intake_sklearn/intake_sklearn/source.py in read(self)
         60                    'but version {} has been installed in your current environment.'
         61                   ).format(self.metadata['sklearn_version'], sklearn.__version__)
    ---> 62             raise RuntimeError(msg)
         63 
         64 


    RuntimeError: The model was created with Scikit-Learn version 0.20.1 but version 0.21.3 has been installed in your current environment.
```

## Catalogs

Store models wherever FSSpec can access them. *You will need also install appropriate packages (s3fs, etc.)*


```python
s3_model = cat.s3_model.read()
```


```python
data = [
    85.5,  # Max temperature
    6,     # Month
    False, # Holiday
    True,  # Weekend
    True   # home game
]

value = s3_model.predict([data])
```

```
array([448.81569766])
```


## What's next?

* Is pickle the best (or only format)?
    * I've had luck with JSONPickle model files, except DecisionTree
* Add more drivers
    * XGBoost, Keras/Tensorflow, Dask-ML
    
* ONNX getting better
* pipeline viz PR in Sklearn
    * https://github.com/scikit-learn/scikit-learn/pull/14180
