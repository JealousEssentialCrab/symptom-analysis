import angular from 'angular';
import HomePageController from './home/home.page.controller'
import appConfig from './app.config'

angular
    .module('Symptoms', [])
    .config(['$locationProvider', appConfig])
    .controller("HomePageController", HomePageController);