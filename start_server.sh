source envs/dev
cd symptoms_js
npm run-script build
cd ..
cd symptoms
pipenv run flask run
