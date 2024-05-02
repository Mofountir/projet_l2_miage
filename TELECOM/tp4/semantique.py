import binascii
import struct # pour unpack
import socket
import syntaxe

def analyse_semantique(trame):
    """
    Analyse une trame Ethernet :  cf https://fr.wikipedia.org/wiki/Ethernet    
    Input : trame est un tableau d'octets
    """
    print("-"*60)
    print ("\nTrame Ethernet en cours d'analyse ({}): \n{} ... ".format( type(trame), trame[0:10]))
  
    # Analyse du header ETHERNET
    eth_header = trame[0:14]
    #print(eth_header)

    # Analyse de la Charge
    eth_data  = trame[14:34]
    

    # Analyse de la data
    UDP_data = trame[34:42]

    DHCP_data = trame[296:341] #on prend que la partie pertinante
    
    
    # https://docs.python.org/fr/3/library/struct.html | https://docs.python.org/3/library/struct.html#byte-order-size-and-alignment
    eth_mac_dest, eth_mac_src, eth_type = struct.unpack('!6s6sH' , eth_header)
    

    print ('Destination MAC : {}'.format(eth_mac_dest.hex(":"))) # .hex() ssi Python > 3.8
    print ('Source MAC \t: {}'.format(binascii.hexlify(eth_mac_src))) # on refait une chaine du tab de byte.
    if eth_type == 2048:
        print ('EtherType \t: {}'.format("IPv4"))
    #https://fr.wikipedia.org/wiki/EtherType pour savoir quel etherType


    misc, protocole, header_checksum, adresse_source, adresse_destination = struct.unpack('!9ss2s4s4s', eth_data)
    print ('Adresse destination: {} =  {}'.format(adresse_destination.hex(":"), socket.inet_ntoa(adresse_destination))) # .hex() ssi Python > 3.8
    print ('Adresse Sources\t: {} = {}'.format(binascii.hexlify(adresse_source),socket.inet_ntoa(adresse_source))) # on refait une chaine du tab de byte.
    if int(binascii.hexlify(protocole)) == 11:
        print ('protocole \t: {}'.format("UDP"))
    #https://en.wikipedia.org/wiki/List_of_IP_protocol_numbers pour identifier le protocole


    

    source_port, destination_port, xxxx, yyyy = struct.unpack('!HHHH' , UDP_data)

    requesed_IP, x, host_name, xx, nom_client, xxx, vendor  = struct.unpack('!4s2s6s5s18s2s8s' , DHCP_data) # les x ne sont pas interessantes

    

    if destination_port == 7:
        print ('Destination port: {}'.format('ECHO')) 
    if destination_port == 67:
        print ('Destination port: {}'.format("DHCP")) 
        print('Type de message: {}'.format('BOOT Request'))
    if source_port == 68:
        print ('Source port: {}'.format("DHCP"))
    if (source_port >= 1023 and source_port <= 65535):
        print ('Source port: {}'.format("RTP"))
    
    #https://fr.wikipedia.org/wiki/Liste_de_ports_logiciels pour les port

    print ('Adresse IP demandée \t: {} = {}'.format(binascii.hexlify(requesed_IP),socket.inet_ntoa(requesed_IP)))
    print ('Nom du Hôte \t: {}'.format(host_name.decode('utf-8')))
    print ('Nom du client \t: {}'.format(nom_client.decode('utf-8')))
    print ('Vendor Class Identifier \t: {}'.format(vendor.decode('utf-8')))
    print('Liste des requetes \t:')

    i = 0
    while i <= 14:
        requestsHist = trame[343+i]
        print('-({})'.format(requestsHist))
        i += 1

    ##########################################################
    # TODO : Maintenant que vous avez compris il faut analyser la suite de la trame  !!!

#=================================================================
if __name__ == '__main__':
    filename = "XXX.txt"
    filename = "d_req.txt"
    # Analyse syntaxique
    lestrames = syntaxe.analyse_syntaxique(filename)
    # Analyse sémantique 
    for trame in lestrames:
        analyse_semantique(trame)        
