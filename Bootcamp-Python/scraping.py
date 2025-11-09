
class Ville():
    """ Carte d'une ville, regroupant ses attributs,
    ses évènements et ses possessions."""
    def __init__(self, name):
        self.name = str(name)
        self.attributs = {}
        self.events = []
        self.posssessions = []

    def __str__(self):
        return "Carte de la ville : " + self.name

    class Attribut:
        """ Sous classe d'attribut, regroupant une clé, une valeur,
        et le type de la valeur. """
        def __init__(self, key, val, type_val):
            self.key = key
            self.val = val
            self.type_val = type_val

    def addAttribut(self, key, val, type_val):
        """ Ajoute un attribut dans le dictionnaire d'attributs. """
        self.attributs[key] = self.Attribut(key, val, type_val)

    def infos(self):
        """" Display les attributs de la ville. """
        print(self)
        for k, v in self.attributs.items():
            print("\t{} : {}".format(k, v.val))

    def addEvent(self, event):
        """ Ajoute un évènement dans la liste d'events. """
        self.attributs.append(event)

    def addPossession(self, possession):
        """ Ajoute une possession dans la liste des possessions. """
        self.possessions.append(possession)


if __name__ == '__main__':
    """ Script de scrapping des 272 villes les plus peuplées de France sur Wikipedia"""
    import requests, json, re
    from bs4 import BeautifulSoup as btsp

    cities = {} # dictionnaire vide qui accueuillera les villes indexées par leur nom.
    base_url = "https://fr.wikipedia.org"
    src = base_url + "/wiki/Liste_des_communes_de_France_les_plus_peuplées#Communes_de_plus_de_30_000_habitants"
    content = requests.get(src)
    soup = btsp(content.text, "html.parser")
    tableau = soup.find('table', {'class':"wikitable sortable"}).tbody.find_all('tr') # on récupère le tableau de 272 villes

    #dict des attributs qui nous intéressent et leur clé dans le dict d'attributsde chaque ville
    info_list = {
        'Région':('region', 'NP'), 
        'Département':('dept', 'NP'),
        'Arrondissement':('arr', 'NP'),
        'Métropole':('metropole', 'NP'),
        'Chef-lieu':('chef_lieu', 'NP'),
        'Statut':('statut', 'N'),
        'Canton':('canton', 'N'),
        'Intercommunalité':('intercommu', 'N'),
        'Préfet délégué':('prefet', 'NP'),
        'Assemblée délibérante':('ad', 'N'),
        'Président':('president', 'NP'),
        'Maire':('maire', 'NP'),
        'Code postal':('code_postal', 'CD'),
        'Gentilé':('gentile', 'NP'),
        'Populationmunicipale':('population', 'CD'),
        'Densité':('densite', 'hab/km2'),
        'Population aire urbaine':('aire_urbaine', 'CD'),
        'Coordonnées':('coor', 'coordinates'),
        'Altitude':('altitude', 'distance.meter'),
        'Superficie':('superficie', 'surface.kilometer'),
        'Monnaie':('monnaie', 'money.amount.EUR'),
        'Fuseau horaire':('fuseau', 'utc'),
        'Indicatif téléphonique':('tel_code', 'phone.alpha_2'),
        'Site web':('site', 'url')}

    for tr in tableau:
        if tr.td and tr.td.string != '¤\n':
            page = base_url + tr.find('b').a['href'] # construction de la bonne url
            page_content = requests.get(page) # requêrte http sur la page de la ville
            parser = btsp(page_content.text, "html.parser")
            infobox = parser.find('table', {'class':'infobox_v2'}).tbody.find_all('tr') # on récupère le tableau d'infos

            name = tr.find('b').a.string
            rank = int(tr.td.string)
            new_city = Ville(name) # instanciation d'un nouvel objet de type Ville
            new_city.addAttribut('rang', rank, 'ordinal.rank')
            new_city.addAttribut('nom', name, 'NP')
            new_city.addAttribut('tel_code', 33, 'phone.alpha_2')
            for line in infobox:
                if line.find('th', {'scope':'row'}) is not None and line.th.text.strip() in info_list.keys():
                    categorie = line.th.text.strip()
                    if categorie != 'Site web':
                        information = re.sub(r'(hab\.)?(/?km2)?', '', re.sub(r'\(.+\)', '', line.td.text.strip().replace('\n', ', '))).strip()
                    else:
                        information = line.td.a['href'].strip() if line.td.find('a') else line.td.string.strip()
                    new_city.addAttribut(info_list[categorie][0], information, info_list[categorie][1])
            cities[name] = new_city
            new_city.infos()
    my_json = json.dumps(cities, default=lambda o: o.__dict__, ensure_ascii=False)
    print(my_json)