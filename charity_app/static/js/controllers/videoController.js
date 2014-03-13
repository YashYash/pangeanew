function videoController($scope, $http, $routeParams, $sce) {
    console.log($routeParams);

    $http.get('/api/v1/charity_full?format=json').success(function(data) {
        console.log(data);
        console.log(data.objects);
        $scope.videos = data.objects;

        for(var i=0; i < $scope.videos.length; i++) {
            $scope.videos[i].trusted_url = $sce.trustAsResourceUrl($scope.videos[i].video_url);
            console.log($scope.videos[i].trusted_url);
        }
    });


}




