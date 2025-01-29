class exoplanetNode:
  
  # initializer ("constructor") method ------------------------
  def __init__(self, name, OrbRadius, OrbPeriod, year, numJupiters):
    # instance attributes
    self.next = None
    self.ID = name
    self.orbital_radius = OrbRadius
    self.orbital_period = OrbPeriod
    self.discovery_date = year
    self.mass = numJupiters
   # list-support -------------------------------------------
  def remove_after(self):
    temp = self.next
    if temp != None:
       self.next = temp.next
    return temp;

  def insert_after(self, new_node):
    if not isinstance(new_node, exoplanetNode):
         return
    new_node.next = self.next
    self.next = new_node 
   # stringizer ----------------------------------------------
  def __str__(self):
     return "id: " + self.ID + "\nOrbital Radius: " +    str(self.orbital_radius) + "\nOrbital Period: " + str(self.orbital_period) + "\nDiscovery Date:"+ str(self.discovery_date) + "\nMass: " + str(self.mass) 
# END CLASS Node ------------------------------------------
