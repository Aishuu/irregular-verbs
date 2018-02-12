var headerController = function ($scope, $location, $anchorScroll) {
    'use strict';

    $scope.goTo = function (url) {
        var old = $location.hash ();
        $location.hash(url);
        $anchorScroll ();
        $location.hash (old);
    }
};

angular.module ('siteperso').controller ('headerController', ['$scope', '$location', '$anchorScroll', headerController]);
