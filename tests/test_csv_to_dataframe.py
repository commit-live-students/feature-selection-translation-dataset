from unittest import TestCase
import pandas as pd


filepath1 = "./data/test_table.csv"
filepath2 = "./data/user_table.csv"

class TestCsv_to_dataframe(TestCase):
    def test_csv_to_dataframe(self):
        from build import csv_to_dataframe
        res = csv_to_dataframe(filepath1)
        self.assertTrue(isinstance(res, pd.DataFrame))
        res = csv_to_dataframe(filepath2)
        self.assertTrue(isinstance(res, pd.DataFrame))

    def test_merge_dataframe(self):
        from build import csv_to_dataframe, merge_dataframe
        res1 = csv_to_dataframe(filepath1)
        self.assertTrue(isinstance(res1, pd.DataFrame))
        res2 = csv_to_dataframe(filepath2)
        self.assertTrue(isinstance(res2, pd.DataFrame))
        res = merge_dataframe(res1, res2, 'user_id')
        self.assertTrue(isinstance(res, pd.DataFrame))

    def test_dtype_category(self):
        from build import dtype_category, csv_to_dataframe, merge_dataframe
        res1 = csv_to_dataframe(filepath1)
        self.assertTrue(isinstance(res1, pd.DataFrame))
        res2 = csv_to_dataframe(filepath2)
        self.assertTrue(isinstance(res2, pd.DataFrame))
        res = merge_dataframe(res1, res2, 'user_id')
        new_res = dtype_category(res, ["user_id", "sex", "country", "date", "source", "device", "browser_language", "ads_channel", "browser"])
        self.assertTrue(isinstance(new_res, pd.DataFrame))

    def test_correlation_list(self):
        from build import correlation_list, csv_to_dataframe, merge_dataframe
        res1 = csv_to_dataframe(filepath1)
        self.assertTrue(isinstance(res1, pd.DataFrame))
        res2 = csv_to_dataframe(filepath2)
        self.assertTrue(isinstance(res2, pd.DataFrame))
        res = merge_dataframe(res1, res2, 'user_id')
        new_res = correlation_list(res)
        self.assertTrue(isinstance(new_res, list))

    def test_multi_power(self):
        from build import multi_power, csv_to_dataframe, merge_dataframe
        res1 = csv_to_dataframe(filepath1)
        self.assertTrue(isinstance(res1, pd.DataFrame))
        res2 = csv_to_dataframe(filepath2)
        self.assertTrue(isinstance(res2, pd.DataFrame))
        res = merge_dataframe(res1, res2, 'user_id')
        column_list = ["age"]
        list_of_powers = [0.5, 2, 3]
        new_res = multi_power(res, column_list, list_of_powers)
        self.assertTrue(isinstance(new_res, pd.DataFrame))


    def test_log(self):
        from build import log, csv_to_dataframe, merge_dataframe
        res1 = csv_to_dataframe(filepath1)
        self.assertTrue(isinstance(res1, pd.DataFrame))
        res2 = csv_to_dataframe(filepath2)
        self.assertTrue(isinstance(res2, pd.DataFrame))
        res = merge_dataframe(res1, res2, 'user_id')
        new_res = log(res, ["age"])
        self.assertTrue(isinstance(new_res, pd.DataFrame))

    def test_loglog(self):
        from build import loglog, csv_to_dataframe, merge_dataframe
        res1 = csv_to_dataframe(filepath1)
        self.assertTrue(isinstance(res1, pd.DataFrame))
        res2 = csv_to_dataframe(filepath2)
        self.assertTrue(isinstance(res2, pd.DataFrame))
        res = merge_dataframe(res1, res2, 'user_id')
        new_res = loglog(res, ["age"])
        self.assertTrue(isinstance(new_res, pd.DataFrame))

    def test_remove_inf_values(self):
        from build import remove_inf_values, csv_to_dataframe, merge_dataframe
        res1 = csv_to_dataframe(filepath1)
        self.assertTrue(isinstance(res1, pd.DataFrame))
        res2 = csv_to_dataframe(filepath2)
        self.assertTrue(isinstance(res2, pd.DataFrame))
        res = merge_dataframe(res1, res2, 'user_id')
        new_res = remove_inf_values(res, "age_loglog")
        self.assertTrue(isinstance(new_res, pd.DataFrame))

    def test_best_k_features(self):
        from build import best_k_features, csv_to_dataframe, merge_dataframe
        res1 = csv_to_dataframe(filepath1)
        self.assertTrue(isinstance(res1, pd.DataFrame))
        res2 = csv_to_dataframe(filepath2)
        self.assertTrue(isinstance(res2, pd.DataFrame))
        res = merge_dataframe(res1, res2, 'user_id')
        predictors = ["age", "age^0.5", "age^2", "age^3", "age_log", "age_loglog"]
        target = 'test'
        new_res = best_k_features(res, predictors, target, 3)
        self.assertTrue(isinstance(new_res, list))


    def test_rf_rfe(self):
        from build import rf_rfe, csv_to_dataframe, merge_dataframe
        res1 = csv_to_dataframe(filepath1)
        self.assertTrue(isinstance(res1, pd.DataFrame))
        res2 = csv_to_dataframe(filepath2)
        self.assertTrue(isinstance(res2, pd.DataFrame))
        res = merge_dataframe(res1, res2, 'user_id')
        predictors = ["age", "age^0.5", "age^2", "age^3", "age_log", "age_loglog"]
        target = 'test'
        new_res = rf_rfe(res, predictors, target)
        self.assertTrue(isinstance(new_res, list))