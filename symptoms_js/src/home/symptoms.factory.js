
SymptomsFactory.$inject = ['$http'];

export default function SymptomsFactory($http){

    function getSymptoms(){
        return $http.get('/symptoms')
    }

    function getTopDiagnosis(symptom){
        return $http.get('/diagnoses/top_diagnosis?symptom=' + symptom.symptom_name);
    }

    function incrementWeight(symptom, diagnosis){
        return $http.post('/diagnoses/increment_weight', {'symptom': symptom, 'diagnosis': diagnosis})
    }

    function getAllDiagnoses(symptom){
        return $http.get('/diagnoses/?symptom=' + symptom);
    }

    return{
        getSymptoms: getSymptoms,
        getTopDiagnosis: getTopDiagnosis,
        incrementWeight: incrementWeight,
        getAllDiagnoses: getAllDiagnoses
    }

}