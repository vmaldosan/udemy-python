import ducks

flock = ducks.Flock()
donald = ducks.Duck()
daisy = ducks.Duck()
lucas = ducks.Duck()
alfred = ducks.Duck()
mallard = ducks.Duck()
goose = ducks.Duck()
percy = ducks.Penguin()

flock.addDuck(donald)
flock.addDuck(daisy)
flock.addDuck(lucas)
flock.addDuck(alfred)
flock.addDuck(percy)
flock.addDuck(mallard)
flock.addDuck(goose)

flock.migrate()
