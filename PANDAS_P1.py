import pandas as pd
brown = {'Student': ('Ice Bear','Panda','Grizzly'),'Math':(80,95,79)}
white = {'Student': ('Ice Bear','Panda','Grizzly'),'Electronics':(85,81,83)}
black = {'Student': ('Ice Bear','Panda','Grizzly'),'GEAS':(90,79,93)}
bears = {'Student': ('Ice Bear','Panda','Grizzly'),'ESAT':(93,89,88)}
brwndf = pd.DataFrame(brown,columns=['Student','Math'])
whtdf = pd.DataFrame(white,columns=['Student','Electronics'])
blckdf = pd.DataFrame(black,columns=['Student','GEAS'])
bearsdf = pd.DataFrame(bears,columns=['Student','ESAT'])
grizzly = brwndf.merge(whtdf, how = 'inner')
panda = grizzly.merge(blckdf, how = 'inner')
icebear = panda.merge(bearsdf, how = 'inner')
bare = pd.melt(icebear, id_vars=['Student'], value_vars = ['Math','Electronics','GEAS','ESAT'],var_name='Subject',value_name = 'Grade' )