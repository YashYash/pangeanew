var videoApp = angular.module('videoApp', ['ngRoute', 'ngResource']);

videoApp.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
    $routeProvider.
        when('/', { templateUrl: '/static/views/stream.html', controller: 'videoController' })
}]);
