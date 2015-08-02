"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
Brand.query.filter_by(id=8).one()

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()

# Get all models that are older than 1960.
Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Note the above query produced the following, which apparently works, but encounters
# a problem with handling the data that is not in standard 'ascii' format
#
# 2015-08-02 14:36:41,407 INFO sqlalchemy.engine.base.Engine SELECT brands.id AS brands_id, brands.name AS brands_name, brands.founded AS brands_founded, brands.headquarters AS brands_headquarters, brands.discontinued AS brands_discontinued 
# FROM brands 
# WHERE brands.founded < ? OR brands.discontinued IS NULL
# 2015-08-02 14:36:41,408 INFO sqlalchemy.engine.base.Engine (1950,)
# [<Brand id=1 id=Ford>, <Brand id=2 id=Chrysler>, Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# UnicodeEncodeError: 'ascii' codec can't encode character u'\xeb' in position 20: ordinal not in range(128)

# Get all brands with that are either discontinued or founded before 1950.

Brand.query.filter(db.or_(Brand.founded < 1950, Brand.discontinued == None)).all()


# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    # commented out working query with year specified as 1963, substituted parameter year
    # m = db.session.query(Model.name, Model.brand_name, Brand.headquarters).join(Brand).filter(Model.year == 1963)
    m = db.session.query(Model.name, Model.brand_name, Brand.headquarters).join(Brand).filter(Model.year == year)
    for name, brand, hq in m.all():
    	print name, brand, hq

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    b = db.session.query(Model.brand_name, Model.name).all()

    for brand, name in b:
    	print brand, name

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# The returned value is a query that looks like:
# SELECT brands.id AS brands_id, brands.name AS brands_name, brands.founded AS brands_founded, brands.headquarters AS brands_headquarters, brands.discontinued AS brands_discontinued 
# FROM brands
# The data type is:
# type <class 'flask_sqlalchemy.BaseQuery'> 

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
# An association table is a third table that makes it possible to represent a
# many-to-many relationship between 2 tables.
# For example, if students have many teachers and teachers have many students,
# these 2 tables could be linked through a third classes table. There is a 
# one-to-many relationship between students and classes (each student can have
# many classes) and a 1-to-many relationship between teachers and classes (each teacher
# can have many classes), and the relationship between teachers and students can be
# found through each of their relationships with classes.
