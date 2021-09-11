import pandas as pd

PARAMS_FOR_DB = ['PG_HOST', 'PG_BASE', 'PG_USER', 'PG_PASSWORD']


class Config:
    CONFIG_FILE = 'settings/config.txt'

    def get_params(self, params: list = None):
        df_conf = pd.read_csv(self.CONFIG_FILE, sep='=')
        params_dict = {}
        if not params:
            params_dict = df_conf.set_index('param').T.to_dict('records')
            pass
        else:
            for idx, param in enumerate(df_conf['param']):
                if param in params:
                    params_dict[param] = df_conf['value'][idx]
                    params.remove(param)
                if len(params) == 0:
                    break
        return params_dict

    def get_all_params(self):
        return self.get_params()

    def get_params_for_db(self):
        return self.get_params(PARAMS_FOR_DB)
