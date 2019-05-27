from bulletbox import BulletBox
from gun import Gun
from person import Person

bulletBox = BulletBox(5)

gun = Gun(bulletBox)

person = Person(gun)

person.fire()
person.fire()
person.fire()
person.fire()
person.fire()
person.fire()

person.fillGun(3)
person.fire()