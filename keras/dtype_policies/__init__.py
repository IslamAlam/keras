from keras import backend
from keras.dtype_policies import dtype_policy
from keras.dtype_policies.dtype_policy import FloatDTypePolicy
from keras.dtype_policies.dtype_policy import QuantizedDTypePolicy


def get(identifier):
    from keras.saving import serialization_lib

    if identifier is None:
        return dtype_policy.dtype_policy()
    if isinstance(identifier, (FloatDTypePolicy, QuantizedDTypePolicy)):
        return identifier
    if isinstance(identifier, dict):
        return serialization_lib.deserialize_keras_object(identifier)
    if isinstance(identifier, str):
        if "int8" in identifier:
            return QuantizedDTypePolicy(identifier)
        else:
            return FloatDTypePolicy(identifier)
    try:
        return FloatDTypePolicy(backend.standardize_dtype(identifier))
    except:
        raise ValueError(
            "Cannot interpret `dtype` argument. Expected a string "
            f"or an instance of DTypePolicy. Received: dtype={identifier}"
        )
