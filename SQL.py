import mysql.connector


def resetDataBase():
    connection = mysql.connector.connect(
        user='root',
        password='Lapepagordacomemucho1997.'

    )

    cursor = connection.cursor(buffered=True)

    # CREATE DATABASE SQUEMA
    cursor.execute('DROP DATABASE IF EXISTS realStatedb')
    cursor.execute('CREATE DATABASE IF NOT EXISTS realStatedb;')
    cursor.execute('USE realStatedb;')

    # CREATE TABLES IN THE RIGHT ORDER, FIRST TABLES WITH NO PRIMARY KEYS,THEN FOLLOW THE ARROWS...
    # 1st: EXTRAS,CONTACTS,TRANSACTIONTYPES,LOCATIONS,TYPES OF PROPERTIES,
    # 2ndREALSTATEAGENCIES, since contains Foreign keys to contacts
    # 3d PROPERTIES
    # 4th:PROPERTIES_EXTRAS,REALSTAEAGENCIES_PROPERTIES

    sqlCommand = '''
        CREATE TABLE IF NOT EXISTS EXTRAS(
            extra_Id INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,
            extraName VARCHAR(50) NOT NULL UNIQUE
        )ENGINE=InnoDB;
    '''
    cursor.execute(sqlCommand)
    connection.commit()

    sqlCommand = '''
        CREATE TABLE IF NOT EXISTS LOCATIONS(
            location_Id INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,
            locationName VARCHAR(50) NOT NULL UNIQUE
        )ENGINE=InnoDB;
    '''
    cursor.execute(sqlCommand)
    connection.commit()

    sqlCommand = '''
        CREATE TABLE IF NOT EXISTS TRANSACTIONTYPES(
            transactionType_Id INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,
            transactionTypeName VARCHAR(50) NOT NULL UNIQUE
        )ENGINE=InnoDB;
    '''
    cursor.execute(sqlCommand)
    connection.commit()

    sqlCommand = '''
        CREATE TABLE IF NOT EXISTS TYPESOFPROPERTIES(
            typeOfProperty_Id INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,
            typeOfPropertyName VARCHAR(50) NOT NULL UNIQUE
        )ENGINE=InnoDB;
    '''
    cursor.execute(sqlCommand)
    connection.commit()

    sqlCommand = '''
        CREATE TABLE IF NOT EXISTS CONTACTS(
            contact_Id INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,
            telephoneNumber VARCHAR(50) NOT NULL UNIQUE,
            email  VARCHAR(50) NOT NULL UNIQUE
        )ENGINE=InnoDB;
    '''
    cursor.execute(sqlCommand)
    connection.commit()

    sqlCommand = '''
        CREATE TABLE IF NOT EXISTS REALSTATEAGENCIES(
            realStateAgency_Id INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,
            realStateAgencyName VARCHAR(50) NOT NULL UNIQUE,
            realStateAgencyAdress VARCHAR(50) NOT NULL UNIQUE,
            contact_Id_FK INT,
            FOREIGN KEY (contact_Id_FK) REFERENCES CONTACTS (contact_Id)
        )ENGINE=InnoDB;
    '''
    cursor.execute(sqlCommand)
    connection.commit()
    sqlCommand = '''
        CREATE TABLE IF NOT EXISTS PROPERTIES(
        property_Id INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,
        price INT,
        bathrooms INT NOT NULL,
        bedrooms INT NOT NULL,
        realStateReference VARCHAR(50) NOT NULL UNIQUE,
        descriptionn  VARCHAR(5000),
        garage BIT NOT NULL,
        terraceArea INT,
        ConstructedArea INT,
        plotSizeArea INT,
        outsideArea INT,
        onSale BIT,
        location_Id_FK INT,
        typeOfProperTy_Id_FK INT,
        transactionType_Id_FK INT,
        FOREIGN KEY (location_Id_FK) REFERENCES LOCATIONS(location_Id),
        FOREIGN KEY (typeOfProperty_Id_FK) REFERENCES TYPESOFPROPERTIES (typeOfProperty_Id),
        FOREIGN KEY (transactionType_Id_FK) REFERENCES TRANSACTIONTYPES (transactionType_Id)
        )ENGINE=InnoDB;'''
    cursor.execute(sqlCommand)
    connection.commit()

    sqlCommand = '''  CREATE TABLE IF NOT EXISTS PROPERTIES_EXTRAS(
        Id INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,
        property_Id INT  NOT NULL,
        extra_id INT NOT NULL,
        FOREIGN KEY (property_Id) REFERENCES PROPERTIES(property_Id),
        FOREIGN KEY (extra_Id) REFERENCES EXTRAS (extra_Id)
        )ENGINE=InnoDB;'''
    cursor.execute(sqlCommand)
    connection.commit()

    sqlCommand = ''' CREATE TABLE IF NOT EXISTS REALSTATEAGENCIES_PROPERTIES(
        Id INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,
        property_Id INT  NOT NULL,
        realStateAgency_id INT NOT NULL,
        FOREIGN KEY (property_Id) REFERENCES PROPERTIES(property_Id),
        FOREIGN KEY (realStateAgency_Id) REFERENCES REALSTATEAGENCIES (realStateAgency_Id)
        )ENGINE=InnoDB;'''
    cursor.execute(sqlCommand)
    connection.commit()
    connection.close()


def populateLocationsAndReturnPK(locationObject):
    connection = mysql.connector.connect(
        user='root',
        password='Lapepagordacomemucho1997.',
        database='realStatedb'
    )

    cursor = connection.cursor()
    sqlCommand = "INSERT INTO LOCATIONS (locationName) VALUES (%s)"
    cursor.execute(sqlCommand, (locationObject.locationName,))
    connection.commit()
    # once the data is populated I would like to extract the tuple's PK
    pkFromRow = returnPrimaryKeyLastTupleFromTable(cursor, locationObject.tableName)
    return pkFromRow

    connection.close()


def returnPrimaryKeyLastTupleFromTable(cursor, tablename):
    try:
        sqlCommand = "SELECT LAST_INSERT_ID() FROM " + tablename
        cursor.execute(sqlCommand)
        result = cursor.fetchone()[0]
    except Exception as e:
        print("Error executing SQL query:", e)
        result = None

    return result


def populateContactsAndReturnPK(contactObject):
    connection = mysql.connector.connect(
        user='root',
        password='Lapepagordacomemucho1997.',
        database='realStatedb'
    )
    telephone = contactObject.telephoneNumber
    email = contactObject.email
    valuesToBePassedAsTuple = (telephone, email)
    cursor = connection.cursor()
    sqlCommand = "INSERT INTO CONTACTS (telephoneNumber,email) VALUES (%s,%s)"
    cursor.execute(sqlCommand, valuesToBePassedAsTuple)
    connection.commit()
    pkFromRow = returnPrimaryKeyLastTupleFromTable(cursor, contactObject.tableName)
    return pkFromRow
    connection.close()


def populateTypeOfProperiesAndReturnPK(typeOfPropertiesObject):
    connection = mysql.connector.connect(
        user='root',
        password='Lapepagordacomemucho1997.',
        database='realStatedb'
    )

    cursor = connection.cursor()
    sqlCommand = "INSERT INTO TYPESOFPROPERTIES (typeOfPropertyName) VALUES (%s)"
    cursor.execute(sqlCommand, (typeOfPropertiesObject.typeOfPropertyName,))
    connection.commit()
    pkFromRow = returnPrimaryKeyLastTupleFromTable(cursor, typeOfPropertiesObject.tableName)
    return pkFromRow
    connection.close()


def populateTransactionTypesAndReturnPk(transactionTypesObject):
    connection = mysql.connector.connect(
        user='root',
        password='Lapepagordacomemucho1997.',
        database='realStatedb'
    )

    cursor = connection.cursor()
    sqlCommand = "INSERT INTO TRANSACTIONTYPES (transactionTypeName) VALUES (%s)"
    cursor.execute(sqlCommand, (transactionTypesObject.transactionTypeName,))
    connection.commit()
    pkFromRow = returnPrimaryKeyLastTupleFromTable(cursor, transactionTypesObject.tableName)
    return pkFromRow
    connection.close()


def populateExtrasAndReturnListPKs(ExtraObject):
    connection = mysql.connector.connect(
        user='root',
        password='Lapepagordacomemucho1997.',
        database='realStatedb'
    )

    cursor = connection.cursor()
    sqlCommand = "INSERT INTO EXTRAS (extraName) VALUES (%s)"
    cursor.execute(sqlCommand, (ExtraObject.extraName,))
    connection.commit()
    pkFromRow = returnPrimaryKeyLastTupleFromTable(cursor, ExtraObject.tableName)
    return pkFromRow
    connection.close()


def populateRealStateAgenciesAndReturnPK(realStateAgencyObject):
    connection = mysql.connector.connect(
        user='root',
        password='Lapepagordacomemucho1997.',
        database='realStatedb'
    )

    cursor = connection.cursor()
    sqlCommand = "INSERT INTO REALSTATEAGENCIES (realStateAgencyName,realStateAgencyAdress,contact_Id_FK) VALUES (%s,%s,%s)"
    realStateAgencyName = realStateAgencyObject.realStateAgencyName
    realStateAgencyAdress = realStateAgencyObject.realStateAgencyAdress
    contact_Id_FK = realStateAgencyObject.contact_Id_FK
    valuesToBePassedAsTuple = (realStateAgencyName, realStateAgencyAdress, contact_Id_FK)
    cursor.execute(sqlCommand, valuesToBePassedAsTuple)
    connection.commit()
    pkFromRow = returnPrimaryKeyLastTupleFromTable(cursor, realStateAgencyObject.tableName)
    return pkFromRow
    connection.close()


def populatePropertiesAndReturnPK(propertyObject):
    connection = mysql.connector.connect(
        user='root',
        password='Lapepagordacomemucho1997.',
        database='realStatedb'
    )

    cursor = connection.cursor()
    sqlCommand = "INSERT INTO PROPERTIES (price,bathrooms,bedrooms,realStateReference,descriptionn,garage,terraceArea,constructedArea,plotSizeArea,location_Id_FK,typeOfProperty_Id_FK,transactionType_Id_FK) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    price = propertyObject.price
    bathrooms = propertyObject.bathrooms
    bedrooms = propertyObject.bedrooms
    realStateReference = propertyObject.realStateReference
    description = propertyObject.description
    garage = propertyObject.garage
    terraceArea = propertyObject.terraceArea
    constructedArea = propertyObject.constructedArea
    plotSizeArea = propertyObject.plotSizeArea
    location_Id_FK = propertyObject.location_Id_FK
    typeOfProperty_Id_FK = propertyObject.typeOfProperty_Id_FK
    transactionType_Id_FK = propertyObject.transactionType_Id_FK

    valuesToBePassedAsTuple = (
    price, bathrooms, bedrooms, realStateReference, description, garage, terraceArea, constructedArea, plotSizeArea,
    location_Id_FK, typeOfProperty_Id_FK, transactionType_Id_FK)
    cursor.execute(sqlCommand, valuesToBePassedAsTuple)
    connection.commit()
    pkFromRow = returnPrimaryKeyLastTupleFromTable(cursor, propertyObject.tableName)
    return pkFromRow
    connection.close()


def populateProperties_Extras(properties_ExtrasObject):
    connection = mysql.connector.connect(
        user='root',
        password='Lapepagordacomemucho1997.',
        database='realStatedb'
    )
    property_Id = properties_ExtrasObject.property_Id
    extra_Id = properties_ExtrasObject.extra_Id
    values = (property_Id, extra_Id)
    cursor = connection.cursor()
    sqlCommand = "INSERT INTO PROPERTIES_EXTRAS (property_Id,extra_Id) VALUES (%s,%s)"
    cursor.execute(sqlCommand, values)
    connection.commit()
    connection.close()

def populateRealStateAgencies_Propertites(realStateAgencies_PropertiesObject):
    connection = mysql.connector.connect(
        user='root',
        password='Lapepagordacomemucho1997.',
        database='realStatedb'
    )
    property_Id = realStateAgencies_PropertiesObject.property_Id
    realStateAgency_Id = realStateAgencies_PropertiesObject.realStateAgency_Id
    values = (property_Id, realStateAgency_Id)
    cursor = connection.cursor()
    sqlCommand = "INSERT INTO REALSTATEAGENCIES_PROPERTIES (property_Id,realStateAgency_Id) VALUES (%s,%s)"
    cursor.execute(sqlCommand, values)
    connection.commit()
    connection.close()
