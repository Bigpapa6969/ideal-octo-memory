from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Death(Scene):
    quips = [
        "You died. You kinda suck at this game!",
        "Bummer - try again!",
        "I have a small iguana that's better at this game!",
        "Did you lag? Or do you just suck",
        "Why you lose?"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])

        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            # be sure to print out the last scene
        current_scene.enter()


class FirstDoor(Scene):
    def enter(self):
        print(dedent("""You are trapped in a maze and there are three doors; a fire door, a snake door, and a dragon 
        door choose wisely which door you take."""))

        choice = input("> ")
        if choice.lower() == "fire":
            print(dedent("""The fire burns you what were you expecting?"""))
            return 'death'

        elif choice.lower() == "snake":
            print(dedent("""You open the door and see a bunch of rattle snakes around the floor you try to get past
            them, but you get bit and die from the poison."""))
            return 'death'

        elif choice.lower() == "dragon":
            print(dedent("""You open the door and see a huge dragon ready to breath fire on you, but he feels pity for
            you so he decides to let you go through to the next level."""))
            return ''

        else:
            print("not an option")
            return 'first_door'


class GuessTheLockCode(Scene):
    def enter(self):
        print(dedent("""After thr dragon flew you over to the next section of this escape room you see a keypad and 
        it asks for a number between 1-1000 and if you take more than 10 attempts you die."""))

        code = randint(1, 1000)
        guess = input("> ")
        guess = int(guess)
        guesses = 0
        while guess != code & guesses < 10:
            guesses += 1
            if guess > code:
                print("your guess was higher than the code you have " + (10-guesses) + " guesses left")
            else:
                print("your guess was lower than the code you have " + (10-guesses) + " guesses left")
            guess = input("> ")
            guess = int(guess)
        if guess == code:
            print(dedent("""The code buzzed a green light and you were let through."""))
            return 'room_of_danger'
        else:
            print(dedent("""The code buzzed a red light and you got zapped in the head."""))
            return 'death'

class RoomOfDanger(Scene):
    pass




class Finished(Scene):

    def enter(self):
        print("YOU WON!!! Nice job!")
        return 'finished'


class Map(object):
    scenes = {
        'first_door': FirstDoor(),
        'guess_the_lock_code': GuessTheLockCode(),
        'room_of_danger': RoomOfDanger(),
        'death': Death(),
        'finished': Finished(),

    }




 def __init__(self, start_scene):
    self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)

        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map("first_door")
a_game = Engine(a_map)
a_game.play()