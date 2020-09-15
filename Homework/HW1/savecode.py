# Hold Code
# Attempts at nicer colors
my_colors=['darkred', 'tomato', 'sienna', 'darkorange', 'goldenrod', 
           'yellowgreen', 'darkgreen', 'seagreen', 'steelblue', 'mediumblue', 'darkviolet']
viridis = cm.get_cmap('viridis', len(rulingsDFbyTrack))
colors = viridis(np.arange(viridis.N))
color = cm.viridis_r(np.linspace(.4,.8,11))
rulingsDFbyTrack.plot(kind='bar', label='Index', stacked=True, color=color)

cMap = plt.cm.gist_earth
Ncolors = min(cMap.N,11)
mapcolors = [cMap(int(x*cMap.N/Ncolors)) for x in range(Ncolors)]

mapcolors = cm.rainbow(np.linspace(0,1,11))

#rulingsDFbyTrack.plot(kind='bar', label = 'Index', cmap=viridis)
rulingsDFbyTrack.plot(kind='bar', colormap='Paired', stacked=True)
rulingsDFbyTrack.plot(kind='bar', label='Index', color=mapcolors)
rulingsDFbyTrack.plot(kind='bar', label = 'Index' , cmap=plt.cm.get_cmap('viridis', len(rulingsDFbyTrack)))
rulingsDFbyTrack.plot(kind='bar', color = plt.cm.Paired(np.arange(len(rulingsDFbyTrack))))

