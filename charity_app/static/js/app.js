var videoApp = angular.module('videoApp', ['ngRoute', 'ngResource']);

videoApp.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
    $routeProvider.
        when('/', { templateUrl: '/static/views/stream.html', controller: 'videoController' }).
        when('/charity/:id', { templateUrl: '/static/views/charity_details.html', controller: 'charityController' }).
        when('/giver/:id', { templateUrl: '/static/views/giver_details.html', controller: 'giverController' });

}]);
