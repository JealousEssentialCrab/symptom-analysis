
HomePageController.$inject = ['SymptomsFactory']

export default function HomePageController(SymptomsFactory){
    var vm = this;

    vm.pageTitle = "Please pick a symptom.";

    SymptomsFactory.getSymptoms().then(function(response){
        vm.symptoms = response.data;
        vm.selectedSymptom = response.data[0];
    });

    vm.getTopDiagnosis = function(){
        SymptomsFactory.getTopDiagnosis(vm.selectedSymptom).then(function(response){
            vm.topDiagnosis = response.data;
        });
    }

    vm.confirmDiagnosis = function(){
        SymptomsFactory.incrementWeight(vm.selectedSymptom.symptom_name,
         vm.topDiagnosis.diagnosis_name);
        vm.diagnosisConfirmed = true
    }

    vm.confirmNewDiagnosis = function(){
        SymptomsFactory.incrementWeight(vm.selectedSymptom.symptom_name,
        vm.selectedDiagnosis.diagnosis_name);
        vm.diagnosisConfirmed = true
    }

    vm.denyDiagnosis = function(){
        vm.diagnosisDenied = true;
        SymptomsFactory.getAllDiagnoses(vm.selectedSymptom.symptom_name)
            .then(function(response){
                vm.fullDiagnosisList = response.data;
                vm.selectedDiagnosis = response.data[0];
        })
    }

    vm.resetSelection = function(){
        vm.topDiagnosis = null;
        vm.selectedDiagnosis = null;
        vm.diagnosisConfirmed = false;
        vm.diagnosisDenied = false;
    }
}