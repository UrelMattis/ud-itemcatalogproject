# imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Category, Base, Item, User

# Bind the engine to the metadata of the Base class
engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create dummy user

"""
User data that will be used for the showTeam page.


Each user consist of their name, email, and picture.
"""

newUser1 = User(name="John Doe", email="johndoe@johndoe.com",
                picture='https://cdn2.iconfinder.com/data/icons/website-icons/512/User_Avatar-512.png')
session.add(newUser1)
session.commit()

# teams for baskbetball

"""
Team data that will be used for the basketball category.


Each team consist of the user id, team name, description, level, and category.
"""

sport1 = Category(user_id=1, name="Basketball")

session.add(sport1)
session.commit()

team1 = Item(user_id=1, name="LA Lakers", description="Team in Los Angeles, CA",
             level="Professional", category=sport1)

session.add(team1)
session.commit()


team2 = Item(user_id=1, name="Rutgers University",
             description="Team in New Jersey", level="Collegiate", category=sport1)

session.add(team2)
session.commit()

team3 = Item(user_id=1, name="Boston Celtics",
             description="Team in Boston, MA", level="Professional", category=sport1)

session.add(team3)
session.commit()

# teams for football

"""
Team data that will be used for the football category.


Each team consist of the user id, team name, description, level, and category.
"""

sport2 = Category(user_id=1, name="Football")

session.add(sport2)
session.commit()


team1 = Item(user_id=1, name="University of North Carolina",
             description="Team in Chapel Hill, NC", level="Collegiate", category=sport2)

session.add(team1)
session.commit()

team2 = Item(user_id=1, name="Atlanta, Falcons",
             description="Team inAtlanta, GA", level="Professional", category=sport2)

session.add(team2)
session.commit()

team3 = Item(user_id=1, name="Arizona Cardinals",
             description="Team in Arizona", level="Professional", category=sport2)

session.add(team3)
session.commit()

print "dummy information has been added!"
