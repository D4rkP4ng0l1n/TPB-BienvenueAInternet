# TPB-BienvenueAInternet

1.5 Questions intermédiaires

1. Quelle est la structure de la ligne GET / HTTP/1.1 ? Quels sont les trois éléments et leur rôle ?
   
2. Pourquoi faut-il appuyer deux fois sur Entrée pour que le serveur réponde ? Que représente cette ligne vide dans le protocole HTTP ?
   
3. Que se passe-t-il si vous oubliez cette ligne vide ? Le serveur répond-il quand même ?
   
4. Que signifie le code 200 OK dans la réponse ? Qu’indique un code 404 ou 301 ?

5. Quelle est la toute première ligne envoyée par le serveur ? Que contientelle ?
    
6. Relevez les entêtes présents dans la réponse (Content-Type, Content-Length, etc.) : à quoi servent-ils ?
    
7. Quelle est la première ligne non entête du corps ? À quoi reconnaît-on la séparation ?
    
8. Que se passe-t-il si vous tapez une URL invalide (ex : GET /truc HTTP/1.1) ? Quel est le code de retour ?
    
9. Le contenu retourné dans ce cas est-il aussi du HTML ? Que contient-il exactement ?

    
2.1.2 Questions

1. Est-ce que votre client (navigateur, curl, telnet…) reçoit bien une réponse ? Quel contenu voyez-vous à l’écran ?
   
2. Quelle est la structure exacte du message que vous renvoyez (statut, entêtes, ligne vide, corps) ?
   
3. Que se passe-t-il si vous changez Content-Length: 12 en une autre valeur ?
   
4. Que se passe-t-il si vous omettez complètement cette ligne ?
   
5. Que se passe-t-il si vous supprimez la ligne vide entre les entêtes et le message ? Le navigateur ou le client affiche-t-il encore quelque chose ?
   
6. Le message s’affiche-t-il dans telnet ? Et dans curl ? Et dans un navigateur ? Pourquoi certains outils sont-ils plus stricts que d’autres ?


2.2.3 Questions

1. Quelle est la structure de la ligne de requête HTTP reçue côté serveur ? Quels sont les trois éléments que vous devez extraire ?
   
2. Que se passe-t-il si la ligne est mal formée (ex. : vide ou incomplète) ? Comment éviter une erreur dans votre code ?
   
3. Que contient exactement la variable chemin ? Est-ce toujours ce que l’utilisateur a tapé dans l’URL ?
   
4. Que fait votre serveur si la méthode reçue est autre que GET ? Par exemple : POST, FOO, TEAPOT ?
   
5. Que se passe-t-il si le chemin n’est pas reconnu (ex. : /truc) ? Quel message retournez-vous ? Est-il lisible ?
    
6. Le message 404 Not Found est-il suffisant comme réponse ? Pourriez-vous y ajouter un texte plus explicite ?
    
7. Est-ce que les chemins /motd, /motd/, et /motd ?x=42 sont identiques ? Comment les différencier ou les normaliser ?
    
8. Pour ajouter un nouveau chemin comme /bonjour, que faut-il modifier dans votre code ? Est-ce que votre structure est facilement extensible ?
    
9. Que pourrait-il se passer si un utilisateur tape une URL comme /../../etc/passwd ? Pourquoi est-ce potentiellement dangereux ?
    
10. Est-ce que vous traitez le chemin comme une simple chaîne de caractères, ou comme une ressource contrôlée ? Quelles protections pourriez-vous ajouter pour éviter les comportements inattendus ?


2.3.2 Questions

1. Quelle est la ligne exacte reçue par le serveur quand un client appelle /date ? Comment repérez-vous ce chemin ?
   
2. Comment déterminez-vous que la requête est terminée ? Quelle est l’utilité de la ligne vide à la fin de la requête ?
   
3. Que contient la réponse retournée par votre serveur ? Est-ce que la date change à chaque appel ?
   
4. Quel champ d’entête est indispensable pour que la réponse soit bien comprise par le client ? Que se passe-t-il si vous oubliez Content-Length ?
   
5. Que se passe-t-il si Content-Length est incorrect (trop petit ou trop grand) ? Testez avec curl, telnet, et un navigateur.

6. Le corps de votre réponse contient-il des caractères spéciaux ou des retours à la ligne (\n) ? Comment sont-ils affichés selon le client utilisé ?
   
7. Que renvoie votre serveur si un autre chemin est demandé, par exemple /time ou /now ? Est-ce prévu ? Que se passe-t-il ?
   
8. Est-ce que le serveur répond de manière fiable même si deux clients se connectent successivement ? Et en même temps ?
    
9. Pourriez-vous ajouter un autre chemin dynamique (comme /uptime) ? Quelles informations pourraient être utiles à afficher ?
    
10. Que faudrait-il faire pour rendre ce serveur un peu plus “propre” ou modulaire ? Est-ce que le code pourrait être réorganisé pour gérer plusieurs routes dynamiques plus facilement ?
