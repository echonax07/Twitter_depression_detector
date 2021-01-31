from ipyaggrid import Grid


## print the dataframe in interactive mode
def show_df(df):
    
    column_defs = [{'field': c} for c in df.columns[:]]

    grid_options = {
        'columnDefs': column_defs
    }

    g = Grid(grid_data=df,
             grid_options=grid_options, 
             sync_grid=True,
            columns_fit='auto')

    display(g)