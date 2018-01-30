import angular from 'angular';
import HomePageController from './home/home.page.controller'
import SymptomsFactory from './home/symptoms.factory'
import appConfig from './app.config'

angular
    .module('Symptoms', [])
    .config(['$locationProvider', appConfig])
    .controller("HomePageController", HomePageController)
    .factory("SymptomsFactory", SymptomsFactory)