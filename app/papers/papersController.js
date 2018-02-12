var papersController = function ($scope, $http) {
    'use strict';

    $http.get ("./assets/data/papers.json")
    .success (function (response) {
        $scope.papers = response;
    });

    $http.get ("./assets/data/confReview.json")
    .success (function (response) {
        $scope.confs = response;
    });
};

angular.module ('siteperso').controller ('papersController', ['$scope', '$http', papersController]);
