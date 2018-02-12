'use strict';

var irregularverbs = angular.module ('irregularverbs', ['ngRoute']);

irregularverbs.config (['$routeProvider',
    function ($routeProvider) {
        $routeProvider.when('/', {
            templateUrl: 'app/main/main.html',
            controller: 'mainController'
        }).otherwise ({
            redirectTo: '/'
        });
    }]);
