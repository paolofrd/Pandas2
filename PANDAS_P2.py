import pandas as pd
dic = {'Box':('Box1','Box1','Box1','Box2','Box2','Box2'),'Dimension':('Length','Width','Height','Length','Width','Height'),'Value':(6,4,2,5,3,4)}
df = pd.DataFrame(dic, columns = ['Box','Dimension','Value'])
df2 = df.pivot(index = 'Box',columns='Dimension',values = 'Value')
df2['Volume'] = df2.Length*df2.Height*df2.Width