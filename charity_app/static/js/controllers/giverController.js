function giverController($scope, $http, $routeParams) {
    console.log($routeParams);

    $http.get('/api/v1/giver/' + $routeParams.id + '?format=json').success(function(data) {
        console.log(data);
        $scope.giver = data;
        console.log($scope.giver);

        $scope.giver.trusted_url = $sce.trustAsResourceUrl($scope.giver.video_url);
            console.log($scope.giver.trusted_url);

    })
}