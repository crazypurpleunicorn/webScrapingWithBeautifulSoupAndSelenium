"""urllib is a library(package) which contains several modules for working with URLs
urrlib.request is one of them which defines functions and classes which help in opening URLs"""

import urllib.request;
from bs4 import BeautifulSoup, NavigableString;
import classes
import scriptToGetExtrasFromARatherLargeDescription
import SQL
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def getSoupObjectFromHeadlessBrowser(url):
    options = Options()
    options.add_argument('headless=new')
    chromedriver_path = 'C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python39\\chromedriver.exe'
    driver_service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=driver_service)
    driver.get(url)
    page_contents = driver.page_source
    beautifulSoupObjecfFirstPage = BeautifulSoup(page_contents, 'html5lib')
    return beautifulSoupObjecfFirstPage


def getSoupObjectFromURL(URL):
    # get Response object from given URL
    urlResponse = urllib.request.urlopen(URL)
    # create beautifulsoup object and parse the contents of the response
    BeautifulSoupObject = BeautifulSoup(urlResponse, 'html5lib')
    return BeautifulSoupObject


def goUpByNumberOfTimes(originTag,
                        howManyTimes):  # looks for parent tag(howManyTimes=1), grandpa(howManyTimes=2)...and So on
    i = 0
    while i < howManyTimes:
        originTag = originTag.parent
        i = i + 1;
    return originTag  # return descendent


def findAllTagsFromSoupObjectGivenTagTypeAndClass(soupObject, tagType, _class):
    tagList = soupObject.find_all(tagType, class_=_class)

    return tagList


def obtainListOfAbsoluteLinksFromListOfRelativeLink(listOfRelativeLinks):
    listOfAbsoluteLinks = []
    for link in listOfRelativeLinks:
        relativeLink = link.get('href')
        absoluteLink = getFullURL(relativeLink)
        listOfAbsoluteLinks.append(absoluteLink)
    return listOfAbsoluteLinks


def getFullURL(relativeURL):  # The links scraped from the 1st page are relative, so we need to complete them.
    completeURL = 'https://www.firstmallorca.com' + relativeURL
    return completeURL


def scrapeAndReturnDictionaryOfBoxWithIcons(soupObjectFromProperty):
    # there is only one element with class info and inner_space, thus it is easyly identifiable.
    divListWithClassInfoInnerspace = soupObjectFromProperty.find_all(class_="info inner_space")
    divWithClassInfoInnerspace = divListWithClassInfoInnerspace[0]

    childrenOfDivWithClassInfoInnerspace = divWithClassInfoInnerspace.contents

    divWithClassRowDescendantFromDivWithClassInnerspace = childrenOfDivWithClassInfoInnerspace[2]
    fatherOfAllSquares = divWithClassRowDescendantFromDivWithClassInnerspace.div

    dictionary = {}
    childrenOfFatherOfAllSquares = fatherOfAllSquares.children
    for child in childrenOfFatherOfAllSquares:
        lowerDiv = child.div
        contentsFromLowerDiv = lowerDiv.contents
        key = str(contentsFromLowerDiv[1].contents[0])
        value = str(contentsFromLowerDiv[2].contents[0])
        dictionary[key] = value
    return dictionary


def scrapeAndReturnTelephoneAndEmail(soupObjectFromProperty):
    divListWithGivenHref = soupObjectFromProperty.find_all(href="tel:+34971007007")
    try:
        email = str(divListWithGivenHref[0].parent.contents[6].span.string)
        telephone = str(divListWithGivenHref[0].contents[1].string)


    except Exception:
        telephone = str(divListWithGivenHref[1].contents[1].string)

    return telephone, email


def scrapeAndReturnTypeOfProperty(soupObjectFromProperty):
    divListWithClassOfferTypePrimary = soupObjectFromProperty.find_all(class_="offer_type primary")
    divWithClassOfferTypePrimaryObjective = divListWithClassOfferTypePrimary[0]
    typeOfProperty = str(divWithClassOfferTypePrimaryObjective.string)  # bs4.element.NavigableString to string
    return typeOfProperty


def scrapeAndReturnLocation(soupObjectFromProperty):
    tagListWithClassLocation = soupObjectFromProperty.find_all(class_="location")
    objectiveDivWithClassLocation = tagListWithClassLocation[0]
    try:
        location = str(
            objectiveDivWithClassLocation.span.a.string)  # most common structure to get to link element where location is
    except AttributeError:
        location = str(
            objectiveDivWithClassLocation.span.string)  # in some pages other format appears omitting the link element directly
    return location


def scrapeAndReturnPrice(soupObjectFromProperty):
    tagListWithClassRowBaselineKeepMpriceref = soupObjectFromProperty.find_all(class_='row baseline keep m_price_ref')
    firstDivWithClassRowBaselineKeepMpriceref = tagListWithClassRowBaselineKeepMpriceref[0]

    if (firstDivWithClassRowBaselineKeepMpriceref.contents[0].get('class')[2]) == 'keep':
        objective = firstDivWithClassRowBaselineKeepMpriceref.div.contents[1].div.string
        objective = str(objective)

    elif (firstDivWithClassRowBaselineKeepMpriceref.contents[0].get('class')[2]) == 'price':
        objective = firstDivWithClassRowBaselineKeepMpriceref.div.div.contents[1].div.div.string
        objective = str(objective)
    if objective == 'P.O.A':
        objective = None
    return objective


def scrapeAndReturnRealStateReference(soupObjectFromProperty):
    tagListWithClassRefidRight = soupObjectFromProperty.find_all(class_='ref_id right')
    objective = tagListWithClassRefidRight[0].string
    realStateReference = str(objective)
    return realStateReference


def scrapeAndReturnDescription(soupOjectFromProperty):
    tagListWithClassContent = soupOjectFromProperty.find_all(class_='content')
    divClassContentObjective = tagListWithClassContent[0]
    divClassContentObjectivesChildren = divClassContentObjective.contents
    howManyChildren = len(divClassContentObjectivesChildren)
    for child in divClassContentObjectivesChildren:
        if not isinstance(child, NavigableString):
            if len(child.contents) == 1:
                description = str(child.string)
            else:
                # sometimes the paragraph has sons
                stringtoprint = ""
                for childchild in child.contents:
                    stringtoprint = stringtoprint + str(childchild)
                description = stringtoprint
            return description


def scrapeAndPrintAll(soupObjectFromProperty):
    telephone, email = scrapeAndReturnTelephoneAndEmail(soupObjectFromProperty)
    dictionaryOfBoxWithIcons = scrapeAndReturnDictionaryOfBoxWithIcons(soupObjectFromProperty)
    typeOfProperty = scrapeAndReturnTypeOfProperty(soupObjectFromProperty)
    price = scrapeAndReturnPrice(soupObjectFromProperty)
    location = scrapeAndReturnLocation(soupObjectFromProperty)
    realStateReference = scrapeAndReturnRealStateReference(soupObjectFromProperty)
    description = scrapeAndReturnDescription(soupObjectFromProperty)
    print(telephone)
    print(email)
    print(dictionaryOfBoxWithIcons)
    print(typeOfProperty)
    print(price)
    print(location)
    print(realStateReference)
    print(description)


def iterateThroughtAllAbsoluteLinkListMakeSoupObjectAndScrapeAndPrint(listOfAbsoluteLinks):
    for link in listOfAbsoluteLinks:
        bs4ObjectPropertyPage = getSoupObjectFromHeadlessBrowser(link)
        scrapeAndPrintAll(bs4ObjectPropertyPage)
        print('*******************************************************************')


def getListOfAbsoluteLinksFromPropertySearchWebsite(urlFromSearchPropertyPage):
    bs4objectSearchPropertyPageHeadless = getSoupObjectFromHeadlessBrowser(urlFromSearchPropertyPage);
    listOfRelativeLinks = findAllTagsFromSoupObjectGivenTagTypeAndClass(bs4objectSearchPropertyPageHeadless, 'a',
                                                                        'active button')
    listOfAbsoluteLinks = obtainListOfAbsoluteLinksFromListOfRelativeLink(listOfRelativeLinks)
    return listOfAbsoluteLinks


def scrapeOneTimeMaxNumberofPropertySearchWebsites(bs4objectFirstPageHeadless):
    objectivesAscendant = bs4objectFirstPageHeadless.find_all(class_='pagination bg_light inner_space small')
    stringAlmostthere = str(objectivesAscendant[0].div.nav.contents[2].string)
    maxNumberOfProperyWebsites = stringAlmostthere.replace('of ', '')
    return int(maxNumberOfProperyWebsites)


def returnListOfAllLinksOfPropertySearchWebsitesGivenANumber(numberOfLinksInTheList):
    listOfLinks = []
    initialUrl = url = 'https://www.firstmallorca.com/en/search'
    i = 1

    while i <= numberOfLinksInTheList:
        listOfLinks.append(initialUrl)
        if i == 1:
            initialUrl = initialUrl + '/' + str(i)
        else:
            initialUrl = initialUrl.replace(str(i - 1), str(i))
        i = i + 1
    return listOfLinks


def scrapeAndPrintAllGivenAListOfPropertySearchWebsites(listOfAllLinksOfPropertySearchWebsitesGivenANumber):
    counter = 1
    for link in listOfAllLinksOfPropertySearchWebsitesGivenANumber:
        # we find a way to select all links of  every property on the Property Search Website
        listOfAbsoluteLinks = getListOfAbsoluteLinksFromPropertySearchWebsite(link)

        """ Once we know how to scrape the page we will iterate this process for every property/link..."""
        iterateThroughtAllAbsoluteLinkListMakeSoupObjectAndScrapeAndPrint(listOfAbsoluteLinks)

        print('!!!!!!!!!!!!!!!!!!!!!!!!NEXT SEARCH PROPERTY WEBSITE' + str(counter))
        counter = counter + 1


def returnExtrasObjectsListFromGivenDescription(description):
    dictionary = scriptToGetExtrasFromARatherLargeDescription.returnExtrasDictionaryFromDescription(description)
    listOfExtrasObjects = []
    for key, value in dictionary.items():
        if value == True:
            extraObject = classes.Extras(key)
            listOfExtrasObjects.append(extraObject)
    return listOfExtrasObjects


def scrapeAndCreateObjects(listOfAllLinksOfPropertySearchWebsitesGivenANumber):
    for link in listOfAllLinksOfPropertySearchWebsitesGivenANumber:
        # we find a way to select all links of  every property on the Property Search Website
        listOfAbsoluteLinks = getListOfAbsoluteLinksFromPropertySearchWebsite(link)
        for link in listOfAbsoluteLinks:

            bs4ObjectPropertyPage = getSoupObjectFromHeadlessBrowser(link)
            telephone, email = scrapeAndReturnTelephoneAndEmail(bs4ObjectPropertyPage)
            dictionaryOfBoxWithIcons = scrapeAndReturnDictionaryOfBoxWithIcons(bs4ObjectPropertyPage)
            typeOfProperty = scrapeAndReturnTypeOfProperty(bs4ObjectPropertyPage)
            price = scrapeAndReturnPrice(bs4ObjectPropertyPage)
            location = scrapeAndReturnLocation(bs4ObjectPropertyPage)
            realStateReference = scrapeAndReturnRealStateReference(bs4ObjectPropertyPage)
            description = scrapeAndReturnDescription(bs4ObjectPropertyPage)

            # get all elements out of the dictionary
            bathrooms = dictionaryOfBoxWithIcons.get("Bathrooms")
            bedrooms = dictionaryOfBoxWithIcons.get("Bedrooms")
            terraceArea = dictionaryOfBoxWithIcons.get("Terrace")
            constructedArea = dictionaryOfBoxWithIcons.get("Constructed Area")
            plotSizeArea = dictionaryOfBoxWithIcons.get("Plot size")
            garage = dictionaryOfBoxWithIcons.get("Parking")
            # Format data according to PROPERTIES
            # garage column in table PROPERTIES is BIT, so it must be a 0 or a 1
            if garage == '✓':
                garage = 1
            else:
                garage = 0
            if terraceArea != None:
                try:
                    terraceArea = int(terraceArea.replace('m', '').replace(',', ''))
                except:
                    terraceArea = int(terraceArea.replace('m', ''))

            if constructedArea != None:
                try:
                    constructedArea = int(constructedArea.replace('m', '').replace(',', ''))
                except:
                    constructedArea = int(constructedArea.replace('m', ''))
            if plotSizeArea != None:
                try:
                    plotSizeArea = plotSizeArea = int(plotSizeArea.replace('m', '').replace(',', ''))
                except:
                    int(plotSizeArea.replace('m', ''))
            if price != None:
                price=price.replace(',','').replace('€','')

            # all TransactionType will be SELL
            transactionType = "SELL"
            realStateAgencyName = 'firstMallorca'
            realStateAgencyAdress = 'fmAdress'

            # certain objects have to be created first and their SQL scripts run in order to populate the database
            # these following five objects will be populated as tuples in their Tables and since the given tuple's primary key
            # is of interest to other tables, we also need a way to store it for the coming objects of other tables

            objectLocations = classes.Locations(location)
            # foreign key for PROPERTIES table
            location_Id_FK = SQL.populateLocationsAndReturnPK(objectLocations)

            objectContacts = classes.Contacts(telephone, email)
            # foreign key for REALSTATEAGENCIES table
            contact_Id_FK = SQL.populateContactsAndReturnPK(objectContacts)

            objectTypeOfProperties = classes.TypeOfProperties(typeOfProperty)
            # foreign key for PROPERTIES table
            typeOfProperty_Id_FK = SQL.populateTypeOfProperiesAndReturnPK(objectTypeOfProperties)

            objectTransactionTypes = classes.TransactionTypes(transactionType)
            # foreign key for PROPERTIES table
            transactionType_Id_FK = SQL.populateTransactionTypesAndReturnPk(objectTransactionTypes)

            # CREATE EXTRAS OBJECTS
            listOfExtrasObjects = returnExtrasObjectsListFromGivenDescription(description)
            listOfExtrasForeignKey = []
            for extraObject in listOfExtrasObjects:
                # foreign key for PROPERTIES_EXTRAS
                extra_Id = SQL.populateExtrasAndReturnListPKs(extraObject)
                listOfExtrasForeignKey.append(extra_Id)

            # following objects need a FK value

            objectRealStateAgencies = classes.RealStateAgencies(realStateAgencyName, realStateAgencyAdress,contact_Id_FK)
            # foreign key for REALSTATEAGENCIES_PROPERTIES
            realStateAgency_Id = SQL.populateRealStateAgenciesAndReturnPK(objectRealStateAgencies)

            objectProperties = classes.Properties(price, bathrooms, bedrooms, realStateReference, description, garage,
                                                  terraceArea, constructedArea, plotSizeArea, location_Id_FK,
                                                  typeOfProperty_Id_FK, transactionType_Id_FK)
            # foreign keys for REALSTATAGENCIES_PROPERTIES an PROPERTIES_EXTRAS
            property_Id = SQL.populatePropertiesAndReturnPK(objectProperties)

            for extra_id_FK in listOfExtrasForeignKey:
                objectProperties_Extras = classes.Properties_Extras(property_Id, extra_id_FK)
                SQL.populateProperties_Extras(objectProperties_Extras)

            objectRealStateAgencies_Properties = classes.RealStateAgencies_Properties(property_Id, realStateAgency_Id)
            SQL.populateRealStateAgencies_Propertites(objectRealStateAgencies_Properties)

            print('hi')
