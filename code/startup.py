import brails
#import InventoryGenerator:
from brails.InventoryGenerator import InventoryGenerator
location='Coronita, CA' # 'Gaziantep, TR'
# Initialize InventoryGenerator:
invGenerator = InventoryGenerator(
  location=location, nbldgs=9, randomSelection=True,
  GoogleAPIKey="")

# Run InventoryGenerator to generate an inventory for the entered location:
# To run InventoryGenerator for all enabled attributes set attributes='all':
# 'buildingheight','chimney','erabuilt','garage','numstories','occupancy',
# 'roofcover','roofeaveheight','roofshape','roofpitch'
invGenerator.generate(attributes=
['occupancy','erabuilt','garage','numstories','buildingheight'])

# Output generated inventory to ..\data\:
df=invGenerator.inventory
df.to_csv('../data/'+location+'.csv')
