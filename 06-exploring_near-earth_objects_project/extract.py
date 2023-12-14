"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    with open(neo_csv_path, 'r') as fin:
        reader = csv.DictReader(fin)
        neos = []


        for elem in reader:
            designation = elem['pdes']
            #check for empty name
            if elem['name']=='': name = None
            else: name = elem['name']
            #check for empty diameter and convert to float
            try: diameter = float(elem['diameter'])
            except ValueError: diameter = float('nan')
            #convert to bool
            if bool(elem['pha']) and elem['pha']=='Y': hazardous = True
            else: hazardous = False
            # Define NearEarthObject
            neo = NearEarthObject(designation=designation, name=name,
                                  diameter=diameter, hazardous=hazardous)
            neos.append(neo)

    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    approaches = []
    with open(cad_json_path, 'r') as fin:
        cad_json = json.load(fin)
        cad_data = cad_json['data']
        for cad_datum in cad_data:
            designation = cad_datum[0]
            time = cad_datum[3]
            distance = cad_datum[4]
            velocity = cad_datum[7]
            # Define CloseApproach
            approach = CloseApproach(designation=designation, time=time, 
                                distance=distance, velocity=velocity)
            approaches.append(approach)
    return approaches
