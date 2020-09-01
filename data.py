import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# import fire

def read_data(fname: str):
    df = pd.read_excel(f"{fname}.xlsx", index_col=0, header=0, skiprows=[0])
    return df

def process_data(df: pd.DataFrame, factor: int = 100):
    df_group = df.transform(lambda x: x / factor).round().groupby('x')

    df_group = pd.concat([df_group.mean(), df_group.var(), df_group.min(), df_group.max()], axis=1)
    df_group.columns = ['mean', 'var', 'min', 'max']
    df_group = df_group.reset_index()
    return df_group.transform(lambda x: factor * x)

def table_html(X: np.ndarray):
    row_labels = ['min', 'max', r'$\Delta$']
    col_labels = []
    vals = []

    for i in range(9):
        x = X[np.where((X[:,0] > (i * 1000)) & (X[:,0] <= ((i+1) * 1000)))]
        if len(x):
            col_labels.append('%d - %d' % (i*1000, (i+1)*1000))
            vals.append([x[:,1].min(), x[:,1].max(), x[:,1].max() - x[:,1].min()])
        else:
            break

    df = pd.DataFrame(np.array(vals).transpose().round(2), index=row_labels, columns=col_labels)
    html = df.to_html()
    return html, df

def plot_data(X: np.ndarray):
    fig, ax = plt.subplots(1,1)
    ax.plot(X[:,0], X[:,1])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.title('Messung')
    plt.show()
    # return fig

def plot_data_with_table(df: pd.DataFrame):#, df_table: pd.DataFrame):
    X = df.to_numpy()
    fig, ax = plt.subplots(1,1)
    ax.plot(X[:,0], X[:,1])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.title('Messung')

    col_labels = []
    vals = []

    for i in range(9):
        x = X[np.where((X[:,0] > (i * 1000)) & (X[:,0] <= ((i+1) * 1000)))]
        col_labels.append('%d - %d' % (i*1000, (i+1)*1000))
        if len(x):
            vals.append([x[:,1].min(), x[:,1].max(), x[:,1].max() - x[:,1].min()])
        else:
            break

    vals = np.array(vals).transpose().round(2)
    # x_table = df_table.to_numpy()

    row_labels = ['min', 'max', r'$\Delta$']
    plt.subplots_adjust(left=0.2, bottom=0.4)
    the_table = ax.table(cellText=vals,
                      rowLabels=row_labels,
                      colLabels=col_labels,
                      loc='bottom', bbox=[0.0,-0.6,1,.28])
    # plt.show()
    # plt.savefig('fig.png')
    return fig

def main(fname: str = 'Beispielwerte aus einer Messung'):
    df = read_data(fname)
    X = df.to_numpy()
    table_html(X)
    plot_data(df)

if __name__ == '__main__':
    # fire.Fire(main)
    main()
