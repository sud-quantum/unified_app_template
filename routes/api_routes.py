"""API routes for JSON endpoints."""
from flask import Blueprint, jsonify, session
import logging

logger = logging.getLogger('flask_app')

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/user', methods=['GET'])
def get_user():
    """Get current user information."""
    try:
        if 'user_id' in session:
            return jsonify({
                'success': True,
                'user': {
                    'id': session['user_id'],
                    'username': session['username']
                }
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Not authenticated'
            }), 401
    except Exception as e:
        logger.error(f"API error in get_user: {str(e)}")
        return jsonify({
            'success': False,
            'message': 'Internal server error'
        }), 500

@api_bp.route('/status', methods=['GET'])
def get_status():
    """Get application status."""
    try:
        return jsonify({
            'success': True,
            'status': 'running',
            'authenticated': 'user_id' in session
        })
    except Exception as e:
        logger.error(f"API error in get_status: {str(e)}")
        return jsonify({
            'success': False,
            'message': 'Internal server error'
        }), 500
