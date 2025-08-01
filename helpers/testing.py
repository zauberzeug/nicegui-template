from enum import Enum


class ResultCombinations(Enum):
    STANDARD = 'standard_result'
    USE_POETRY = 'use_poetry_result'
    USE_ROSYS = 'use_rosys_result'
    USE_PRECOMMIT = 'use_precommit_result'
    USE_POETRY_AND_ROSYS = 'use_poetry_and_rosys_result'
    USE_POETRY_AND_PRECOMMIT = 'use_poetry_and_precommit_result'
    USE_ROSYS_AND_PRECOMMIT = 'use_rosys_and_precommit_result'
    USE_ALL_FEATURES = 'use_all_features_result'
