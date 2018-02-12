var currentController = function ($scope, $http) {
    'use strict';

    $http.get ("./assets/data/current.json")
    .success (function (response) {
        $scope.projects = response;
    });
};

angular.module ('siteperso').controller ('currentController', ['$scope', '$http', currentController]);
