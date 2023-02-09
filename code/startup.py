import brails
#import InventoryGenerator:
from brails.InventoryGenerator import InventoryGenerator

# Initialize InventoryGenerator:
invGenerator = InventoryGenerator(location='Orange, CA',
                                  nbldgs=100, randomSelection=True,
                                  GoogleAPIKey="AIzaSyBOuFNQ82pIHrk5kyE6N5Yeg_028gDwc2Q")

# Run InventoryGenerator to generate an inventory for the entered location:
# To run InventoryGenerator for all enabled attributes set attributes='all':
invGenerator.generate(attributes=['numstories','roofshape','buildingheight'])

# View generated inventory:
invGenerator.inventory
