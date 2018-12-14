#!/bin/bash

#$1 user id
#$2 repo source
#$3 name repo dest


#add this to docker file
echo "172.17.0.1:5432:dtb:gitdtz:password" > /root/.pgpass

chmod 0600 /root/.pgpass
export PGPASSFILE=/root/.pgpass

tokn=$(psql -w -h '172.17.0.1' -U gitdtz  -d dtb -c "SELECT extra_data FROM social_auth_usersocialauth WHERE user_id = $1;" | grep -o -e "{[^}]*}" | jq .access_token | tr -d \" )

IFS="\|" read -r  email username <<< $( psql -w -h '172.17.0.1' -U gitdtz  -d dtb -t -c "SELECT email, username FROM auth_user WHERE id = $1;" | head -1 | tr -d " ")


echo "email: $email"
echo "usernmae: $username"
echo "tokn: $tokn"

if [ "$(curl -X POST https://api.github.com/user/repos -u $username:$tokn -d '{"name":"'$3'"}' | grep message)" == "" ]; then
  echo "Repo Successufully create"
else
  echo -n "Error\nExiting ..."
  exit
fi

git clone "$2" /tmp/"$3"

#continue if failed (no .git folder)
mv /tmp/"$3"/.git /tmp/"$3"/.git.bak || :

cd /tmp/"$3"
git init
git config --local user.name "$username"
git config --local user.email "$email"
git add .
git commit -m "..."
git remote add origin "https://github.com/$username/$3.git"
git push -u "https://$username:$tokn@github.com/$username/$3.git"

cd /app
rm -rf /tmp/"$3"

