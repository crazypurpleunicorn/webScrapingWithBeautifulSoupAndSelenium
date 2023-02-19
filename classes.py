"""Every class written here, represents each of the tables of the relational model and every instance of these Classes a tuple into their respective table"""


class Locations:
    def __init__(self, locationName):
        self.locationName = locationName
        self.tableName="LOCATIONS"
        self.primaryKeyName ="location_Id"


class Extras:
    def __init__(self, extraName):
        self.extraName = extraName
        self.tableName ="EXTRAS"
        self.primaryKeyName ="extra_Id"


class TypeOfProperties:
    def __init__(self, typeOfProperty):
        self.typeOfPropertyName = typeOfProperty
        self.tableName ="TYPESOFPROPERTIES"
        self.primaryKeyName ="typeOfProperty_Id"


class TransactionTypes:
    def __init__(self, transactionType):
        self.transactionTypeName = transactionType
        self.tableName ="TRANSACTIONTYPES"
        self.primaryKeyName ="transactionType_Id"


class Contacts:
    def __init__(self, telephoneNumber, email):
        self.telephoneNumber = telephoneNumber
        self.email = email
        self.tableName ="CONTACTS"
        self.primaryKeyName="contact_Id"


class RealStateAgencies:
    def __init__(self, realStateAgencyName, realStateAgencyAdress, contact_Id_FK):
        self.realStateAgencyName = realStateAgencyName
        self.realStateAgencyAdress = realStateAgencyAdress
        self.contact_Id_FK = contact_Id_FK
        self.tableName ="REALSTATEAGENCIES"
        self.primaryKeyName ="realStateAgency_Id"


class Properties:#outsideArea and on Sale are being omitted
    def __init__(self, price=None, bathrooms=0, bedrooms=0, realStateReference='', description=None, garage='0', terraceArea=None, constructedArea=None, plotSizeArea=None, location_Id_FK=None, typeOfProperty_Id_FK=None, transactionType_Id_FK=None):
        self.price= price
        self.bathrooms=bathrooms
        self.bedrooms=bedrooms
        self.realStateReference=realStateReference
        self.description=description
        self.garage=garage
        self.terraceArea=terraceArea
        self.constructedArea=constructedArea
        self.plotSizeArea=plotSizeArea
        self.location_Id_FK=location_Id_FK
        self.typeOfProperty_Id_FK=typeOfProperty_Id_FK
        self.transactionType_Id_FK=transactionType_Id_FK
        self.tableName = "PROPERTIES"
        self.primaryKeyName ="property_Id"
class Properties_Extras:
    def __init__(self,property_Id, extra_Id):
        self.property_Id=property_Id
        self.extra_Id=extra_Id
        self.tableName ="PROPERTIES_EXTRAS"
        self.primaryKeyName ="Id"


class RealStateAgencies_Properties:
    def __init__(self,property_Id, realStateAgency_Id):
        self.property_Id=property_Id
        self.realStateAgency_Id=realStateAgency_Id
        self.tableName ="REALSTATEAGENCIES_PROPERTIES"
        self.primaryKeyName ="Id"


