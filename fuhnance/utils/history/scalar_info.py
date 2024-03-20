def get_empirical_rule_values(df, dev_col):
    print(df[df[dev_col]<1].shape[0]/df.shape[0])
    print(df[df[dev_col]<2].shape[0]/df.shape[0])
    print(df[df[dev_col]<3].shape[0]/df.shape[0])

def more_info(df, col):
    print(df[col].mean())
    print(df[col].std())
    if '_dev' in col:
        get_empirical_rule_values(df, col)

