from pandas import DataFrame,concat


def series_to_supervised(data, n_in=1,n_out=1,dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    df = DataFrame(data)
    # list 中存放 dataframe 数据 , 用 cancat 合并 df
    cols,names = list(),list()

    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [(f'var{j+1}(t-{i})') for j in range (n_vars)]
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [(f'var{j+1}(t)') for j in range (n_vars)]
        else:
            names += [(f'var{j+1}(t+{j+1})') for j in range(n_vars)]


    agg = concat(cols, axis=1)
    agg.columns = names
    if dropnan:
        agg.dropna(inplace=True)
    return agg