# %%
import dataloader, fitfuns, fitter, plotter
# %%
# load data
df = dataloader.get_data("data.csv")
# plot data
plotter.plot_data(df)
# %%
# fit data
popt = fitter.fit(fitfuns.exp_fit, df["t"], df["A"])
fitted_y = fitter.get_fitted_y(fitfuns.exp_fit, df["t"], popt)
# plot result
plotter.plot_fit(df["t"], df["A"], fitted_y)
# %%
# now the second column
popt = fitter.fit(fitfuns.sin_fit, df["t"], df["B"])
fitted_y = fitter.get_fitted_y(fitfuns.sin_fit, df["t"], popt)
plotter.plot_fit(df["t"], df["B"], fitted_y)
# %%
