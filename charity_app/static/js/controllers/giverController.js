function giverController($scope, $http, $routeParams) {
    console.log($routeParams);

    $http.get('/api/v1/giver/' + $routeParams.id + '?format=json').success(function(data) {
        console.log(data);
        $scope.giver = data;
        console.log($scope.giver)

    })
}