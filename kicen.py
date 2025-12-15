import viz
import vizmat

viz.go()

# ===== Virtuve =====
kicen = viz.add('kicen.obj')
kicen.setPosition(0,0,0)
kicen.setScale(1,1,1)

# ===== Objekti =====
beans = viz.add('beans.obj')
beans.setPosition(-0.3,0.8,0.4)

samalta = viz.add('samalta.obj')
samalta.setPosition(-0.5,0.8,0.4)

cukurs = viz.add('cukurs.obj')
cukurs.setPosition(-0.3,0.8,0.6)

tejkanna = viz.add('tejkanna.obj')
tejkanna.setPosition(0.5,0.8,0.4)

piens = viz.add('piens.obj')
piens.setPosition(0.6,0.8,0.6)
