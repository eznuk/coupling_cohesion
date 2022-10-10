# %%
import config
import dataloader, fitfuns, fitter, plotter
# %%
# load data
df = dataloader.get_data(config.datafile)
# plot data
plotter.plot_data2(df, config.dfmeta)
# fit data
fitter.fit_df(df, config.dfmeta)
# plot result
plotter.plot_df_fits(df, config.dfmeta)
# %%
# now the second column
df2 = dataloader.get_data(config.datafile2)
plotter.plot_data2(df2, config.dfmeta2)
fitter.fit_df(df2, config.dfmeta2)
plotter.plot_df_fits(df2, config.dfmeta2)

# %%
