var mainController = function ($scope) {
    'use strict';

    $scope.pages = [
        {"url": "current", "title": "Ongoing projects"},
        {"url": "papers", "title": "Publications"},
        {"url": "bio", "title": "Bio"},
        {"url": "contact", "title": "Contact"}
    ];
};

angular.module ('siteperso').controller ('mainController', ['$scope', mainController]);
