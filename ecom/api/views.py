from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.permissions import AllowAny

# View for user registration
class RegisterView(APIView):
    # Allow anyone to access this view (even without logging in)
    permission_classes = [AllowAny]

    def post(self, request):
        # Get the data from the request
        serializer = RegisterSerializer(data=request.data)
        
        # Check if the data is valid
        if serializer.is_valid():
            # Save the user
            user = serializer.save()
            
            # Return success response
            return Response({
                "status": "success",
                "message": "User registered successfully!",
                "data": {
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name
                }
            }, status=status.HTTP_201_CREATED)
        
        # If data is invalid, return errors
        return Response({
            "status": "error",
            "message": "Registration failed",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

# View for user login
class LoginView(APIView):
    # Allow anyone to access this view
    permission_classes = [AllowAny]

    def post(self, request):
        # Get the login data
        serializer = LoginSerializer(data=request.data)
        
        # Check if the data is valid
        if serializer.is_valid():
            # Get username and password
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            
            # Try to authenticate the user
            user = authenticate(username=username, password=password)
            
            if user:
                # If authentication is successful, log the user in
                login(request, user)
                
                # Return success response
                return Response({
                    "status": "success",
                    "message": "Login successful!",
                    "data": {
                        "username": user.username,
                        "email": user.email,
                        "first_name": user.first_name,
                        "last_name": user.last_name
                    }
                }, status=status.HTTP_200_OK)
            else:
                # If authentication fails
                return Response({
                    "status": "error",
                    "message": "Invalid username or password"
                }, status=status.HTTP_401_UNAUTHORIZED)
        
        # If login data is invalid
        return Response({
            "status": "error",
            "message": "Login failed",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
