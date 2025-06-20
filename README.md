# TPB-BienvenueAInternet

## 1.5 Questions intermédiaires -  Lire une réponse HTTP

### 1. Quelle est la structure de la ligne `GET / HTTP/1.1` ? Quels sont les trois éléments et leur rôle ?

La ligne `GET / HTTP/1.1` est composée de trois éléments :
- **GET** : méthode HTTP utilisée pour demander une ressource au serveur.
- **/** : chemin absolu de la ressource (ici, la racine).
- **HTTP/1.1** : version du protocole utilisée.

---

### 2. Pourquoi faut-il appuyer deux fois sur Entrée pour que le serveur réponde ? Que représente cette ligne vide dans le protocole HTTP ?

Appuyer deux fois sur Entrée ajoute une **ligne vide (`\r\n`)** qui indique la **fin des en-têtes** de la requête. Sans elle, la requête est incomplète, donc ignorée.

---

### 3. Que se passe-t-il si vous oubliez cette ligne vide ? Le serveur répond-il quand même ?

Le serveur ne répond pas. Le serveur considère que la requête n’est **pas terminée** et attend indéfiniment jusqu’à ce que la connexion soit fermée ou expirée.

---

### 4. Que signifie le code `200 OK` dans la réponse ? Qu’indique un code `404` ou `301` ?

- `200 OK` : La requête a été traitée avec succès.
- `404` : La ressource demandée n'a pas été trouvée.
- `301` : La ressource demandée n'est pas à l'endroit recherchée.

---

### 5. Quelle est la toute première ligne envoyée par le serveur ? Que contient-elle ?

La première ligne de la réponse HTTP, appelée **ligne de statut**, contient : HTTP/1.1 200 OK
Elle indique :
- Le protocole utilisé,
- La version,
- Le code de statut,
- Un message associé.

---

### 6. Relevez les en-têtes présents dans la réponse (Content-Type, Content-Length, etc.) : à quoi servent-ils ?

| En-tête                         | Rôle |
|----------------------------------|------|
| `Content-Type: text/html`        | Type de contenu retourné (ici, HTML). |
| `Transfer-Encoding: chunked`     | La réponse est envoyée en morceaux. |
| `Connection: keep-alive`         | Maintient la connexion ouverte pour d'autres requêtes. |
| `Last-Modified`                  | Date de dernière modification de la ressource. |
| `Cache-Control: max-age=600`     | Durée pendant laquelle la ressource peut être mise en cache. |
| `Expires`                        | Date d’expiration de la ressource. |
| `Vary`                           | La réponse peut varier selon certains en-têtes (compression, user-agent...). |
| `cf-cache-status`                | Statut du cache côté Cloudflare. |
| `Report-To`, `NEL`               | Utilisés pour les rapports d’erreurs réseau. |
| `Server: cloudflare`             | Nom du serveur ou du proxy. |
| `CF-RAY`                         | Identifiant de traçage Cloudflare. |
| `alt-svc`                        | Offre un service alternatif (ex: HTTP/3). |
| `server-timing`                  | Indique des mesures de performance côté serveur. |

---

### 7. Quelle est la première ligne non en-tête du corps ? À quoi reconnaît-on la séparation ?

La première ligne du corps est `cc`. Elle arrive après une **ligne vide (`\r\n`)**. C’est la séparation obligatoire entre les en-têtes et le contenu.

---

### 8. Que se passe-t-il si vous tapez une URL invalide (ex : `GET /truc HTTP/1.1`) ? Quel est le code de retour ?

Le serveur renvoie une réponse d'erreur : 400 Bad Request

---

### 9. Le contenu retourné dans ce cas est-il aussi du HTML ? Que contient-il exactement ?

Oui, c’est une page HTML d’erreur typique, souvent semblable à ceci :

```html
<html>
<head><title>400 Bad Request</title></head>
<body>
<center><h1>400 Bad Request</h1></center>
<hr><center>cloudFlare</center>
</body>
</html>
```

---
    
## 2.1.2 Questions — Implémenter un mini-serveur HTTP (TCP brut)

### 1. Est-ce que votre client (navigateur, curl, telnet…) reçoit bien une réponse ? Quel contenu voyez-vous à l’écran ?

Oui, j’utilise le **navigateur** comme client en accédant à l’URL `http://localhost:8080`.  
À l’écran, le message suivant est affiché : Hello World!

---

### 2. Quelle est la structure exacte du message que vous renvoyez (statut, entêtes, ligne vide, corps) ?

La réponse envoyée par le serveur est structurée ainsi :
- HTTP/1.1 200 OK             ← Ligne de statut
- Content-Type: text/plain    ← Entête
- Content-Length: 12          ← Entête
- Connection: Close           ← Entête
- `                `          ← Ligne vide
- Hello World!                ← Corps

---

### 3. Que se passe-t-il si vous changez `Content-Length: 12` en une autre valeur ?

- Si la valeur est **supérieure** à 12 : aucun effet visible immédiat (le client attend potentiellement plus de contenu).
- Si la valeur est **inférieure** à 12 : le client n'affiche que les **X premiers caractères** du corps.
  - Exemple : `Content-Length: 2` → le navigateur affiche `He`.

---

### 4. Que se passe-t-il si vous omettez complètement cette ligne ?

Sans l’en-tête `Content-Length`, certains clients comme le **navigateur** ou **curl** peuvent :
- Attendre que la connexion se ferme pour déterminer la fin du corps
- Rien afficher du tout si la fermeture n’intervient pas (comportement indéfini selon le client).

---

### 5. Que se passe-t-il si vous supprimez la ligne vide entre les entêtes et le message ? Le navigateur ou le client affiche-t-il encore quelque chose ?

Non. La ligne vide est **obligatoire** pour séparer les **en-têtes** du **corps**.  
Sans elle, le client (navigateur, curl…) ne peut pas **parser** correctement la réponse, et n’affichera **rien** (ou renverra une erreur).

---

### 6. Le message s’affiche-t-il dans telnet ? Et dans curl ? Et dans un navigateur ? Pourquoi certains outils sont-ils plus stricts que d’autres ?

- **Telnet** : Oui, car il affiche **tout ce qui est reçu**, sans interprétation.
- **curl** : Oui, si la réponse est correctement formatée (notamment avec `Content-Length` et la ligne vide).
- **Navigateur** : Oui, mais il est **plus strict** sur le format HTTP (ligne vide, types MIME, etc.).

---

## 2.2.3 Questions - Serveur avec analyse du chemin

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
