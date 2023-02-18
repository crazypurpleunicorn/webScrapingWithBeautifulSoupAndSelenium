"""Objective:given the following paragraph,for example(It could be totally different paragraph)( which is a description of the property):"An exceptional luxury frontline designer villa overlooking the beautiful turquoise waters of the bay of Portals Vells in Sol de Mallorca and its green zone protected coastline. The stylish, modern design of this high-tech villa of exceptional quality offers security and modern comfort on every level. The property is built on a 2.187 m2 plot with garden and features a constructed area of 1.300 m2 as well as 125 m2 of open terraces. With six-bedroom suites, all with breath-taking seaviews, office, underground garaging for 8 cars with a lift access, one small mooring in the adjoining harbour and various areas to entertain and relax as well as direct access to the sea, this property must be viewed to be fully appreciated. From the outstanding 84m2 infinity pool you will have the feeling to be able to swim directly into the sea. Further features of this remarkable villa are underfloor heating, a/c hot cold, double glazing with UV protection, smart home system, security doors as well as a panic room.

I would like to obtain the information about some elements(for example: garage and number of cars in the garage, ¿has lift access?,¿does it have garden?,¿Does it have double glazing? If so¿has the double glazing UV protection?¿Is this a smart home?, ¿Is there a panic room? ). To extract the data, we have to take into account that the paragraph could be an any paragraph, and not necessarily the previous one on my last message. 

With the help of CHATGPT today I learnt lots about regular expressions
"""
import  re


def returnExtrasDictionaryFromDescription(paragraph):
    info = {}

    if re.search(r'\bgarage(?:s)?\b.', paragraph, re.IGNORECASE):
        info['has_garage'] = True
    if re.search(r'\bgarage\b.*?(\d+)(?=\s+(?:car|vehicle)s?)', paragraph, re.IGNORECASE):
        info['garage_capacity'] = int(re.search(r'\bgarage\b.*?(\d+)(?=\s+(?:car|vehicle)s?)', paragraph, re.IGNORECASE).group(1))
    if re.search(r'\blift access\b', paragraph, re.IGNORECASE):
        info['has_lift_access'] = True
    if re.search(r'\bgarden\b', paragraph, re.IGNORECASE):
        info['has_garden'] = True
    if re.search(r'\bdouble glazing\b', paragraph, re.IGNORECASE):
        info['has_double_glazing'] = True
    if re.search(r'\buv protection\b', paragraph, re.IGNORECASE):
        info['double_glazing_uv_protection'] = True
    if re.search(r'\bsmart home\b', paragraph, re.IGNORECASE):
        info['is_smart_home'] = True
    if re.search(r'\bpanic room\b', paragraph, re.IGNORECASE):
        info['has_panic_room'] = True
    if re.search(r'\b(?:indoor|outdoor(?:s))?\s*(?:swimming\s+)?pool(?:s)?\b', paragraph, re.IGNORECASE):
        info['has_swimming_pool'] = True
        if re.search(r'\b(?:indoor|outdoor)\s+(?:pool|pools)\b', paragraph, re.IGNORECASE):
            info['swimming_pool_type'] = re.search(r'\b(indoor|outdoor)\s+(?:pool|pools)\b', paragraph, re.IGNORECASE).group(1)
    if re.search(r'\bsauna\b', paragraph, re.IGNORECASE):
        info['has_sauna'] = True
    if re.search(r'\b(?:sea|lake)\s+view(?:s)?\b', paragraph, re.IGNORECASE):
        info['has_sea_or_lake_view'] = True

    if re.search(r'\bair\s+conditioning\b', paragraph, re.IGNORECASE) or re.search(r'\bair-conditioning\b', paragraph, re.IGNORECASE) or re.search(r'\bAC\b', paragraph):
        info['has_air_conditioning'] = True

    if re.search(r'\bunderfloor\s+heating\b', paragraph, re.IGNORECASE):
        info['has_under_floor_heating'] = True
    if re.search(r'\bcentral\s+heating\b', paragraph, re.IGNORECASE):
        info['has_central_heating'] = True

    if re.search(r'\bfireside\b|\bfireplace\b', paragraph, re.IGNORECASE):
        info['has_fireside_or_fireplace'] = True
    if re.search(r'\btennis court\b', paragraph, re.IGNORECASE):
        info['has_tennis_court'] = True
    if re.search(r'\bbasketball court\b', paragraph, re.IGNORECASE):
        info['has_basketball_court'] = True
    if re.search(r'\bhelipad\b', paragraph, re.IGNORECASE):
        info['has_helipad']=True
    if re.search(r'\bsurveillance\b', paragraph, re.IGNORECASE):
            info['has_surveillance'] = True
    if re.search(r'\balarm\b', paragraph, re.IGNORECASE):
            info['has_alarm'] = True
    if re.search(r'\bviticulture\b', paragraph, re.IGNORECASE):
        info['has_viticulture']=True
    if re.search(r'\bsolar panel(?:s)?\b', paragraph, re.IGNORECASE or re.search(r'\bsolar system(?:s)?\b', paragraph, re.IGNORECASE)):
        info['has_solar'] = True
    if re.search(r'\bbilliard\b', paragraph, re.IGNORECASE):
        info['has_billiard'] = True
    if re.search(r'\bchapel\b', paragraph, re.IGNORECASE):
        info['has_chapel'] = True
    if re.search(r'\bfountain(s)?\b', paragraph, re.IGNORECASE):
        info['has_fountain'] = True
    if re.search(r'\bviews?\s+of\s+(.+?)\b', paragraph, re.IGNORECASE):
        info['has_views_of'] = re.search(r'\bviews?\s+of\s+(.+?)\b', paragraph, re.IGNORECASE).group(1)
    if re.search(r'\bolive\s+trees?\b', paragraph, re.IGNORECASE):
        info['has_olive_trees'] = True
    if re.search(r'\b(?:waterfall|waterfalls)\b', paragraph, re.IGNORECASE):
        info['has_waterfall'] = True
    if re.search(r'\bbodega(?:s)?\b', paragraph, re.IGNORECASE):
        info['has_bodega'] = True
    if re.search(r'\bterrace(?:s)?\b', paragraph, re.IGNORECASE):
        info['has_terrace'] = True
    if re.search(r'\bspa(?:s)?\b', paragraph, re.IGNORECASE):
        info['has_spa'] = True
    if re.search(r'\bfitness\s+(?:area|zone|gym)\b', paragraph, re.IGNORECASE):
        info['has_fitness_area'] = True
    if re.search(r"\bguest's\s+house\b", paragraph, re.IGNORECASE):
        info['has_guest_house'] = True


    return info

paragraph="""This southwest facing new build villa with panoramic sea views and spectacular sunsets is located in one of the most privileged locations in Cala Llamp. The upper floor offers 4 bedrooms, each with ensuite bathroom and stunning sea views from all rooms. On the ground floor you will find the spacious living room which leads to the open plan kitchen and dining room, and in towards the large covered terrace with outdoor kitchen and dining area, overlooking the infinity pool and the Mediterranean sea. At the back of this new built villa is a generously landscaped garden with lawn. In the basement, the property offers spa and fitness area as well as 2 further bedrooms. The spacious garage provides space for 3 cars. All floors are internally connected by a lift. Further features include underfloor heating with heatpump, garden with lawn, Lift, Pool on roofterrace, outdoor kitchen
"""
results=returnExtrasDictionaryFromDescription(paragraph)
for result in results:
    print(result,': ', results[result])
