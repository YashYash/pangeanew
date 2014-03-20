function charityController($scope, $http, $routeParams) {
    console.log($routeParams);
        console.log("hello");

    $http.get('/api/v1/charity/' + $routeParams.id + '?format=json').success(function(data) {

        console.log(data);
        $scope.charity = data;


        for(var i=0; i < data.length; i++) {
            data[i].trusted_url = $sce.trustAsResourceUrl(data.all[i].video_url);
            console.log(data[i].trusted_url);

        }
    });
}